# Todo-list API

A robust Todo-list API built with FastAPI, integrating Supabase for authentication and SQLAlchemy for database interactions.
## Overview

This API enables users to create, read, update, and delete todo lists and tasks, while managing user authentication and session handling.

## Features

* __CRUD Operations__: Full CRUD functionality for todo lists and individual tasks.
* __User Authentication__: Secure user registration and login powered by Supabase.
* __Documentation__: Interactive API docs generated by FastAPI at /docs.
* __Future Enhancements__: Additional features planned for future releases.

## Installation

### Clone the repository:

```
git clone https://github.com/stylub/todo-list-api.git
cd todo-list-api
```

### Set up a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies:
```
pip install -r requirements.txt
```

## Configuration

Set up Environment Variables:
Create a `.env` file in the project root with the following values:

```
    DATABASE_URL=YOUR_SUPABASE_URL
    DATABASE_KEY=YOUR_SUPABASE_KEY
    SQLALCHEMY_DATABASE_URL=YOUR_SQLALCHEMY_DATABASE_URL
```
Replace YOUR_SUPABASE_URL, YOUR_SUPABASE_KEY, and YOUR_SQLALCHEMY_DATABASE_URL with your actual Supabase and database credentials.

## Usage

To run the API server locally:

* Start the server:
```
uvicorn main:app --reload
```
* Access the API at http://127.0.0.1:8000.

* Explore the interactive API documentation:
```
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc
```
