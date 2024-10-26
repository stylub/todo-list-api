from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column

from typing import List
import os

from supabase import create_client

Base = declarative_base()

class DatabaseConfig():
    Session = None
    supabase = None

    def db_init(self):
        db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

        if not db_url: 
            raise ValueError("You must set SQLALCHEMY_DATABASE_URL")
        
        engine = create_engine(db_url)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        Base.metadata.create_all(bind=engine)
        
        URL = os.getenv("DATABASE_URL")
        if not URL:
            raise ValueError("You must set DATABASE_URL")
        
        KEY = os.getenv("DATABASE_KEY")
        if not KEY:
            raise ValueError("You must set DATABASE_KEY")
        
        self.supabase = create_client(URL, KEY)

    def get_supabase_client(self):
        if not self.supabase:
            raise ValueError("Database client isn't initialized")
        
        return self.supabase

db_config = DatabaseConfig()
class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    text_content: Mapped[str]
    description: Mapped[str]
    finished: Mapped[bool] = mapped_column(default=False)
    todo_list_id: Mapped[int] = mapped_column(ForeignKey('todolist.id'))
    todo_list: Mapped['ToDoList'] = relationship('ToDoList', back_populates='taskList')

class ToDoList(Base):
    __tablename__ = 'todolist'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    taskList: Mapped[List['Task']] = relationship('Task', back_populates='todo_list')
    user_id: Mapped[str]
