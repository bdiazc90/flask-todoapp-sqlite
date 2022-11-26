from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
# Instancia de la DB para usar ORM
# db = SQLAlchemy()

# client = MongoClient("mongodb://bdiazc90:brunodiaz1234@ac-pinvamy-shard-00-00.zt2ztcw.mongodb.net:27017,ac-pinvamy-shard-00-01.zt2ztcw.mongodb.net:27017,ac-pinvamy-shard-00-02.zt2ztcw.mongodb.net:27017/?ssl=true&replicaSet=atlas-ubmrkf-shard-0&authSource=admin&retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://bdiazc90:brunodiaz1234@cluster0.zt2ztcw.mongodb.net/?retryWrites=true&w=majority")
db = client

