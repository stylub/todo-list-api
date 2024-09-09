from sqlalchemy.orm import Session
from . import database
from . import models

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def create_todolist(db: Session, todo_list: models.ToDoListBase):
    try:
        db_list = database.ToDoList(title=todo_list.title)
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

def get_all_todo_lists(db: Session):
    try:
        return db.query(database.ToDoList).all()
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