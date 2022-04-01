from database import db


def create_service(player) -> str:
    created_id = db.create(player.dict())
    return created_id


def read_service(player_id: str) -> dict:
    player = db.read(player_id)
    return player


def read_all_service() -> list[dict]:
    players = db.read_all()
    return players


def update_service(player_id: str, update_data) -> int:
    modified_count = db.update(player_id, update_data.dict(exclude_unset=True))
    return modified_count


def delete_service(player_id: str) -> int:
    is_deleted = db.delete(player_id)
    return is_deleted
