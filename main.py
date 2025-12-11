from fastapi import FastAPI, Depends
from schemas import TodoCreate, TodoResponse
from sqlalchemy.orm import Session
from database import sessionlocal, Base, engine
from models import Todo as TodoModel

Base.metadata.create_all(bind=engine)
app = FastAPI()

#Dependency for db session
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

#POST method - create TODO

@app.post("/todos",response_model=TodoResponse)
def create_todo(todo: TodoCreate, db:Session=Depends(get_db)):
    db_todo = TodoModel(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

#GET method - read TODO
@app.get("/fetchall",response_model=list[TodoResponse])
def fetch_all_todos(db:Session=Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

#GET - fetch by id
@app.get("/todos/{todo_id}",response_model=TodoResponse)
def fetch_by_id(todo_id:int, db:Session=Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id==todo_id).first()
    return todo

#PUT method - update TODO
@app.put("/todos_update/{todo_id}")
def update_todo_by_id(todo_id:int,updated:TodoCreate, db:Session=Depends(get_db)):
    data = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    for key, value in updated.dict().items():
        setattr(data, key, value)
    db.commit()
    db.refresh(data)
    return {"message":"Todo updated successfully"}

#DELETE method - delete TODO
@app.delete("/delete/{todo}")
def delete_by_id(todo:int, db:Session=Depends(get_db)):
    data = db.query(TodoModel).filter(TodoModel.id==todo).first()
    db.delete(data)
    db.commit()
    return {"message":"Todo deleted successfully"}
