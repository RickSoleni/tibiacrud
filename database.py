from pymongo import MongoClient
from bson import ObjectId


client = MongoClient('mongodb://root:MongoDB2019!@127.0.0.1:27017')


class Database:
    def __init__(self) -> None:
        self.client = client
        self.database = self.client['tibiacrud']
        self.players_collection = self.database['players']

    def create(self, values: dict) -> str:
        return str(self.players_collection.insert_one(values).inserted_id)

    def read(self, player_id: str) -> dict:
        player_id = ObjectId(player_id)
        player = self.players_collection.find_one({'_id': player_id})
        if player:
            player['_id'] = str(player['_id'])
        return player

    def read_all(self) -> list[dict]:
        players = list(self.players_collection.find())
        for player in players:
            player['_id'] = str(player['_id'])
        return players

    def update(self, player_id: str, update_data: dict) -> int:
        player_id = ObjectId(player_id)
        return self.players_collection.update_one(
            {'_id': player_id}, {'$set': update_data}
        ).modified_count

    def delete(self, player_id: str) -> int:
        player_id = ObjectId(player_id)
        return self.players_collection.delete_one(
            {'_id': player_id}
        ).deleted_count


db = Database()
