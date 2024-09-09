from sqlalchemy.orm import Session
from . import database
from . import models



def create_todolist(db: Session, todo_list: models.ToDoListBase):
    db_list = database.ToDoList(title=todo_list.title)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)

    for task in todo_list.taskList:
        create_new_task(db,task,db_list.id)

    return db_list

def create_new_task(db: Session, task: models.TaskCreate, list_id: int):
    db_task = database.Task(
        text_content=task.text_content,
        todo_list_id = list_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_todo_lists(db: Session):
    return db.query(database.ToDoList).all()

def get_tasks_by_todolist(db: Session, todo_list_id: int):
    return db.query(database.Task).filter(database.Task.todo_list_id == todo_list_id).all()

def get_todo_list_by_id(db: Session, todo_list_id: int):
    return db.query(database.ToDoList).filter(database.ToDoList.id == todo_list_id).first()