from fastapi import FastAPI
from routes.tasks import task

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome'}

app.include_router(task)