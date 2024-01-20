from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome'}

@app.get('/api/tasks')
async def get_tasks():
    return 'all tasks'

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