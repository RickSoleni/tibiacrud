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

app = FastAPI()


@app.get('/')
def hello_world():
    return {'Tibia': 'Rickera OT Server'}


@app.post('/players')
def create_player(player: PlayerInOutSchema) -> JSONResponse:
    create = create_service(player)
    if not create:
        return JSONResponse({'Message': 'Player Creation Error'}, 500)
    return JSONResponse({'Message': 'Player Created', '_id': create}, 201)


@app.get('/player/{player_id}')
def find_player(player_id: str) -> JSONResponse:
    read = read_service(player_id)
    if not read:
        return JSONResponse({'Message': 'Player Not Found'}, 404)
    return PlayerInOutSchema(**read)


@app.get('/players')
def find_players() -> JSONResponse:
    read_all = read_all_service()
    if not read_all:
        return JSONResponse({'Message': 'Players Not Found'}, 404)
    return JSONResponse({'Players': read_all}, 200)


@app.put('/player/{player_id}')
def modify_player(player_id, update_player: PlayerModifySchema):
    update = update_service(player_id, update_player)
    if not update:
        return JSONResponse({'Message': 'Error while reading database'}, 404)
    return JSONResponse({'Message': 'Player Modified'}, 200)


@app.delete('/player/{player_id}')
def delete_player(player_id: str):
    delete = delete_service(player_id)
    if not delete:
        return JSONResponse({'Message': 'Player Not Found'}, 404)
    return JSONResponse({'Message': 'Player Deleted'}, 200)
