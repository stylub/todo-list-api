from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column

from typing import List

SQLALCHEMY_DATABASE_URL = "postgresql://postgres.ndgagzvhqvhuicrdzfpf:vMnF3XNRF30j5PWR@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    text_content: Mapped[str]
    finished: Mapped[bool] = mapped_column(default=False)
    todo_list_id: Mapped[int] = mapped_column(ForeignKey('todolist.id'))
    todo_list: Mapped['ToDoList'] = relationship('ToDoList', back_populates='taskList')

class ToDoList(Base):
    __tablename__ = 'todolist'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    taskList: Mapped[List['Task']] = relationship('Task', back_populates='todo_list')

Base.metadata.create_all(bind=engine)