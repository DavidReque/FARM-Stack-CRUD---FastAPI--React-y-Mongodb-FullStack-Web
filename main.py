from fastapi import FastAPI
from database import get_all_task

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_task()
    return tasks

@app.post('/api/tasks')
async def create_tasks():
    return 'create tasks'

@app.get('/api/tasks/{id}')
async def get_tasks():
    return 'single tasks'

@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'updating tasks'

@app.delete('/api/tasks/{id}')
async def delete_tasks():
    return 'delete tasks'