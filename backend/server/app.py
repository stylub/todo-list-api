from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from typing import List, Annotated

from dotenv import load_dotenv
from .models import Task, ToDoList,ToDoListCreate,UserCreate, User, Tokens,TaskCreate
from . import crud

from .database import db_config
from .database import ToDoList as db_list

from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(_app: FastAPI):
    load_dotenv()
    db_config.db_init()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
   db = db_config.Session()
   try:
        yield db
   finally:
        db.close()

@app.post('/add_todolist', response_model=ToDoListCreate)
def create_todolist(
        todo_list: ToDoListCreate,
        current_user: Annotated[User, Depends(crud.get_user)],
        db = Depends(get_db)
    ):
    return crud.create_todolist(db=db,todo_list=todo_list,current_user=current_user)

@app.post('/todolist/{todolist_id}/tasks', response_model=List[Task])
def read_tasks(todolist_id: int,current_user: Annotated[User, Depends(crud.get_user)], db = Depends(get_db)):
    return crud.get_tasks_by_todolist(db=db,todo_list_id=todolist_id,current_user=current_user)

@app.post('/todolist/{todolist_id}',response_model=ToDoList)
def get_one_todolist(todolist_id: int,current_user: Annotated[User, Depends(crud.get_user)], db = Depends(get_db)):
    return crud.get_todo_list_by_id(db=db,todo_list_id=todolist_id,current_user=current_user)

@app.post('/todolist/{todolist_id}/task/add',response_model=Task)
def add_task_to_todolist(
        todo_list_id: int,
        task: TaskCreate,
        _current_user: Annotated[User, Depends(crud.get_user)],
        db = Depends(get_db)
    ):
    return crud.create_new_task(db,task,todo_list_id)

@app.post('/user/register',response_model=Tokens)
async def user_register(user:UserCreate):
    return await crud.create_user(user)

@app.post('/user/login',response_model=Tokens)
def user_login(user:UserCreate):
    return crud.login(user)

@app.post('/user/refresh',response_model=Tokens)
def user_refresh(refresh_token:str):
    return crud.refresh_session(refresh_token)

@app.post('/user/get')
def user_get(
    current_user: Annotated[User, Depends(crud.get_user)]
    ):
    return current_user