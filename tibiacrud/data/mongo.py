from pymongo import MongoClient
from bson import ObjectId
import os 

mongodb_uri = os.getenv('MONGODB_URI')
class Database:
    def __init__(self, client) -> None:
        self.client = client
        self.database = self.client['tibiacrud']
        self.players_collection = self.database['players']

    def create(self, values: dict) -> str:
        nickname_count = self.players_collection.count_documents(
            {'nickname': values['nickname']}
        )
        if nickname_count > 0:
            return
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
        nickname_count = self.players_collection.count_documents(
            {'nickname': update_data['nickname']}
        )
        if nickname_count > 0:
            return
            
        player_id = ObjectId(player_id)
        return self.players_collection.update_one(
            {'_id': player_id}, {'$set': update_data}
        ).modified_count

    def delete(self, player_id: str) -> int:
        player_id = ObjectId(player_id)
        return self.players_collection.delete_one(
            {'_id': player_id}
        ).deleted_count

if mongodb_uri:
    client = MongoClient(mongodb_uri)
else:
    client = MongoClient('mongodb://root:MongoDB2019!@127.0.0.1:27017')
db = Database(client=client)
