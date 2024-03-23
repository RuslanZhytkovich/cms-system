from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str | None
    token_type: str
