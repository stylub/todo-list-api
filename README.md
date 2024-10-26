# Todo-list API

Todo-list API made with FastAPI.

## Introduction

This project is a Todo-list API built using FastAPI with supabase and sqlalchemy. It allows users to create, read, update, and delete todo-lists. 

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/stylub/todo-list-api.git
    cd todo-list-api
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the API server, use the following command:
```bash
uvicorn main:app --reload
```

The server will start on `http://127.0.0.1:8000`.

To access automatic docs go to `http://127.0.0.1:8000docs#`

## Features

- Create, read, update, and delete todo items.
- User authentication 
- More functionalities to be added.

