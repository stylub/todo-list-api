from pydantic import BaseModel
from typing import List

class TaskBase(BaseModel):
    text_content: str


class Task(TaskBase):
    id: int
    finished: bool = False

    class Config:
      from_attributes = True

class TaskCreate(TaskBase):
  pass

class ToDoListBase(BaseModel):
    title: str
    

class ToDoList(ToDoListBase):
    id: int
    taskList: List[Task]

    class Config:
      from_attributes = True

class ToDoListCreate(ToDoListBase):
    taskList: List[TaskCreate]