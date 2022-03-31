from database import Database
from bson import ObjectId

db = Database()


def create_service(player):
    created_id = db.create(player.dict())
    return str(created_id)


def read_service(player_id: str) -> dict:
    player_id = ObjectId(player_id)
    player = db.read(player_id)
    if player:
        player['_id'] = str(player['_id'])
    return player


def read_all_service():
    players = db.read_all()
    return players


def update_service(player_id: str, update_data):
    player_id = ObjectId(player_id)
    modified_count = db.update(
        player_id, update_data.dict(exclude_unset=True)
    ).modified_count
    return modified_count


def delete_service(player_id: str):
    player_id = ObjectId(player_id)
    is_deleted = db.delete(player_id)
    return is_deleted
