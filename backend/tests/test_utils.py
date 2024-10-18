from unittest.mock import patch

import pytest

from app.utils import find_potential_matches, create_chat_for_matched_users
from app.models import User
from tests.mocked_data import USER1, USER2, USER3, CHAT_ID


@pytest.fixture
def mock_state_manager():
    with patch("app.utils.state_manager") as mock:
        yield mock


def test_find_potential_matches_mock_llm(mock_settings, mock_state_manager):
    mock_settings.mock_llm = True
    mock_state_manager.get_user.return_value = USER3
    mock_state_manager._users = {
        USER1.id: USER1,
        USER2.id: USER2,
        USER3.id: USER3,
    }

    users = mock_state_manager._users
    match = find_potential_matches(USER1.id, "the queen", users)

    assert match is not None
    assert match["match_id"] in [USER2.id, USER3.id]  # It should not match with "1"

    match = find_potential_matches(USER1.id, "coffee maker", users)
    assert match is None


# TODO:
# def test_find_potential_matches_real_llm(mock_settings):
#     mock_settings.mock_llm = False



def test_create_chat_for_matched_users(mock_state_manager):
    mock_state_manager.get_chat_id_from_matched_pairs.return_value = None
    chat_id = create_chat_for_matched_users(USER1.id, USER2.id)
    
    assert chat_id is not None
    mock_state_manager.set_matched_pairs.assert_called_once_with(USER1.id, USER2.id, chat_id)
    


def test_create_chat_for_matched_users_existing(mock_state_manager):
    mock_state_manager.get_chat_id_from_matched_pairs.return_value = CHAT_ID
    chat_id = create_chat_for_matched_users(USER1.id, USER2.id)
    
    assert chat_id == CHAT_ID
    mock_state_manager.set_matched_pairs.assert_not_called()
