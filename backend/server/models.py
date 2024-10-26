from pydantic import BaseModel
from typing import List

class TaskBase(BaseModel):
    text_content: str
    description: str

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

class UserBase(BaseModel):
    email: str
class options():
   email_redirect_to:str = "http://0.0.0.0:8000"
class UserCreate(UserBase):
   password: str
class UserDatabase(UserCreate):
  options: options
  class Config: 
    from_attributes = True
    arbitrary_types_allowed = True
class User(UserBase):
   id: str
   

   class Config:
      from_attributes = True

class Tokens(BaseModel):
   access_token: str
   refresh_token: str