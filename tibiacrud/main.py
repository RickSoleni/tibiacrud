from fastapi import FastAPI
from tibiacrud.routes.player import player_router

app = FastAPI()


app.include_router(player_router)


@app.get('/')
def hello_world():
    return {'Tibia': 'Rickera OT Server'}
