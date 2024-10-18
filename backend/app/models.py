from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    description: str


class MatchRequest(BaseModel):
    user_id: str
    preferences: str


class MatchResponse(BaseModel):
    match: dict
    chat_id: str
    message: str
