# TASK 
# Description
	Create a simple RESTful API using FastAPI for a social networking application
# Functional requirements:
There should be some form of authentication and registration (JWT, Oauth, Oauth 2.0, etc..)

As a user I need to be able to signup and login

As a user I need to be able to create, edit, delete and view posts

As a user I can like or dislike other users’ posts but not my own 

The API needs a UI Documentation (Swagger/ReDoc)
# Установка
1. Склонировать проект
2. запустить виртуальное окружение
3. установить зависимости из requirements.txt
4. Указать путь к базе postgres в файле config.py
5. запустить ювикорн uvicorn main:app
6. перейти на url http://127.0.0.1:8000/docs