from pydantic import BaseModel


class PlayerInOutSchema(BaseModel):
    nickname: str
    level: int
    vocation: str


class PlayersOutSchema(BaseModel):
    players: list[PlayerInOutSchema]


class PlayerModifySchema(BaseModel):
    nickname: str | None
