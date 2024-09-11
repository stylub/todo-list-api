from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from typing import List, Annotated

from dotenv import load_dotenv
from .models import Task, ToDoList,ToDoListCreate,UserCreate, User, Tokens
from . import crud

from .database import db_config

@asynccontextmanager
async def lifespan(_app: FastAPI):
    load_dotenv()
    db_config.db_init()
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
   db = db_config.Session()
   try:
        yield db
   finally:
        db.close()

@app.post('/add_todolist', response_model=ToDoListCreate)
def create_todolist(todo_list: ToDoListCreate, db = Depends(get_db)):
    return crud.create_todolist(db=db,todo_list=todo_list)

@app.get('/todolist', response_model=List[ToDoList])
def get_all_todo_lists(db = Depends(get_db)):
    return crud.get_all_todo_lists(db)

@app.post('/todolist/{todolist_id}/tasks', response_model=List[Task])
def read_tasks(todolist_id: int, db = Depends(get_db)):
    return crud.get_tasks_by_todolist(db, todolist_id)

@app.post('/todolist/{todolist_id}',response_model=ToDoList)
def get_one_todolist(todolist_id: int, db = Depends(get_db)):
    return crud.get_list_with_tasks(db,todolist_id)

@app.post('/user/register/supa',response_model=Tokens)
async def user_register(user:UserCreate):
    return await crud.create_user_supa(user)

@app.post('/user/login',response_model=Tokens)
def user_login(user:UserCreate):
    return crud.login(user)

@app.post('/user/get')
def user_get(
    current_user: Annotated[User, Depends(crud.get_user)]
    ):
    return current_user