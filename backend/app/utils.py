import random
import uuid

from app.config import settings
from app.state import state_manager, StateManager
from app.custom_types import UserID, Users, ChatID, PotentialMatch


def find_potential_matches(user_id: UserID, preferences: str, users: Users) -> PotentialMatch:
    if settings.mock_llm:
        return __mocked_llm_potential_matches(user_id, preferences, users)
    return __llm_potential_matches(user_id, preferences, users)


def __get_user_match_info(state_manager: StateManager, match_id: UserID) -> PotentialMatch:
    user_info = state_manager.get_user(match_id)
    if not user_info:
        return None

    user_info["match_id"] = match_id
    return user_info


def __mocked_llm_potential_matches(user_id: UserID, preferences: str, users: Users) -> PotentialMatch:
    potential_matches = [
        other_id
        for other_id, other_user in users.items()
        if other_id != user_id and (
                preferences.lower() in other_user["description"].lower() or
                other_user["description"].lower() in preferences.lower()
        )
    ]

    if not potential_matches:
        return None

    return random.choice([
        __get_user_match_info(state_manager, match_id)
        for match_id in potential_matches
        if __get_user_match_info(state_manager, match_id)
    ])


def __llm_potential_matches(user_id: UserID, preferences: str, users: Users) -> PotentialMatch:
    return None


def create_chat_for_matched_users(user_id: UserID, match_id: UserID) -> ChatID:
    existing_chat_id = (
            state_manager.get_chat_id_from_matched_pairs(user_id, match_id) or
            state_manager.get_chat_id_from_matched_pairs(match_id, user_id)
    )
    if existing_chat_id:
        return existing_chat_id

    chat_id = str(uuid.uuid4())
    state_manager.set_matched_pairs(user_id, match_id, chat_id)
    return chat_id
