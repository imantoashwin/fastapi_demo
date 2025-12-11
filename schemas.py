from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None # =None is default
    completed: bool | None = False # =False is default

class TodoCreate(TodoBase): #used when creating a row or  data
    pass

class TodoResponse(TodoBase): #used when returning a row or data
    id: int
    class Config:
        orm_mode = True #converts orm data to json