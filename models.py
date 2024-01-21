from pydantic import BaseModel

class Task(BaseModel):
    id: str
    title: str
    decription: str
    completed: bool = False