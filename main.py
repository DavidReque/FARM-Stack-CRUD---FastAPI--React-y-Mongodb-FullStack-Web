from fastapi import FastAPI, HTTPException
from database import get_all_task, create_task, get_one_task, get_one_task_id, delete_task
from models import Task

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_task()
    return tasks

@app.post('/api/tasks', response_model=Task)
async def create_tasks(task: Task):

    task_found = await get_one_task(task.title)
    if task_found:
        raise HTTPException(409, 'La tarea ya existe')

    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, "Algo salio mal")

@app.get('/api/tasks/{id}', response_model=Task)
async def get_tasks(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Tarea con id {id} no encontrada')

@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'updating tasks'

@app.delete('/api/tasks/{id}')
async def delete_tasks(id: str):
    response = await delete_task(id)
    if response:
        return "Se elimino la tarea"
    raise HTTPException(404, f'Tarea con id {id} no encontrada')