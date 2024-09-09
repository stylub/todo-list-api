from fastapi import FastAPI, Depends
from typing import List
from .database import Session
from .models import Task, ToDoList,ToDoListCreate,ToDoListBase
from . import crud
from contextlib import asynccontextmanager

app = FastAPI()

def get_db():
   db = Session()
   try:
        yield db
   finally:
        db.close()

@app.post('/add_todolist', response_model=ToDoListCreate)
def create_todolist(todo_list: ToDoListCreate, db: Session = Depends(get_db)):
    return crud.create_todolist(db=db,todo_list=todo_list)

@app.get('/todolist', response_model=List[ToDoList])
def get_all_todo_lists(db: Session = Depends(get_db)):
    return crud.get_all_todo_lists(db)

@app.post('/todolist/{todolist_id}/tasks', response_model=List[Task])
def read_tasks(todolist_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks_by_todolist(db, todolist_id)

@app.post('/todolist/{todolist_id}',response_model=ToDoList)
def get_one_todolist(todolist_id: int, db: Session = Depends(get_db)):
    return crud.get_list_with_tasks(db,todolist_id)