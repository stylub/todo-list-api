from sqlalchemy.orm import Session
from . import database
from . import models

from .database import db_config
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def create_todolist(
        db: Session, 
        todo_list: models.ToDoListBase,
        current_user: models.User  
        ):
    try:
        db_list = database.ToDoList(title=todo_list.title,user_id=current_user.id)
        db.add(db_list)
        db.commit()
        db.refresh(db_list)

        for task in todo_list.taskList:
            create_new_task(db, task, db_list.id)

        return db_list
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def create_new_task(db: Session, task: models.TaskCreate, list_id: int):
    try:
        db_task = database.Task(
            text_content=task.text_content,
            todo_list_id=list_id
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def get_all_todo_lists(db: Session, current_user: models.User):
    try:
        return db.query(database.ToDoList).filter(database.ToDoList.user_id == current_user.id).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_tasks_by_todolist(db: Session, todo_list_id: int):
    try:
        return db.query(database.Task).filter(database.Task.todo_list_id == todo_list_id).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_todo_list_by_id(db: Session, todo_list_id: int):
    try:
        return db.query(database.ToDoList).filter(database.ToDoList.id == todo_list_id).first()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


def create_user(user:models.UserCreate):
    supabase = db_config.get_supabase_client()

    response = supabase.auth.sign_up({
        "email": user.email,
        "password": user.password 
    })

    return models.Tokens(
        access_token=response.session.access_token,
        refresh_token=response.session.refresh_token
    )

def login(user: models.UserCreate):
    supabase = db_config.get_supabase_client()

    try:
        response = supabase.auth.sign_in_with_password({
            "email": user.email, 
            "password": user.password
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    return models.Tokens(
        access_token=response.session.access_token,
        refresh_token=response.session.refresh_token
    )

def get_user(jwt:str):
    supabase = db_config.get_supabase_client()

    try:
        response = supabase.auth.get_user(jwt)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return models.User(
        id=response.user.id,
        email=response.user.email
    )
