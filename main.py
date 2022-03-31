from models import PlayerInOutSchema, PlayerModifySchema
from fastapi import FastAPI
from starlette.responses import JSONResponse
from services import (
    create_service,
    delete_service,
    read_service,
    read_all_service,
    update_service,
)
from bson import ObjectId

app = FastAPI()


@app.get('/')
def hello_world():
    return {'Tiba': 'Rickera OT Server'}


@app.post('/players')
def create_player(player: PlayerInOutSchema):
    create = create_service(player)
    if not create:
        return JSONResponse({'Message': 'Player Creation Error'}, 500)
    return JSONResponse({'Message': 'Player Created', '_id': create}, 201)


@app.get('/player/{player_id}')
def find_player(player_id: str):
    read = read_service(player_id)
    if not read:
        return JSONResponse({'Message': 'Player Not Found'}, 404)
    return PlayerInOutSchema(**read)


@app.get('/players')
def find_players():
    read_all = read_all_service()
    if not read_all:
        return JSONResponse({'Message': 'Players Not Found'}, 404)
    return read_all


@app.put('/player/{nickname}')
def modify_player(nickname, player: PlayerModifySchema):
    update = update_service(nickname, player)
    if not update:
        return JSONResponse({'Message': 'Error while reading database'}, 404)
    return JSONResponse({'Message': 'Player Modified'}, 200)


@app.delete('/player/{player_id}')
def delete_player(player_id: str):
    delete = delete_service(player_id)
    if not delete:
        return JSONResponse({'Message': 'Player Not Found'}, 404)
    return JSONResponse({'Message': 'Player Deleted'}, 200)
