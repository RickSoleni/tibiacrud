from pydantic import BaseModel


class PlayerInOutSchema(BaseModel):
    nickname: str
    level: int
    vocation: str


class PlayersOutSchema(BaseModel):
    pĺayers: list[PlayerInOutSchema]


class PlayerModifySchema(BaseModel):
    nickname: str | None
