# from flask_sqlalchemy import SQLAlchemy
# # Instancia de la DB para usar ORM
# db = SQLAlchemy()
from pymongo import MongoClient
client = MongoClient("mongodb+srv://bdiazc90:brunodiaz1234@cluster0.zt2ztcw.mongodb.net/?retryWrites=true&w=majority")
db = client.todoapp