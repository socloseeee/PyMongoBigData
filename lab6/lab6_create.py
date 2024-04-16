from pymongo import MongoClient
import datetime

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Выбор базы данных
db = client['test']

# 1. Создание коллекции и добавление документов
collection = db['selling']

docs = [
    {"name": "Nexus One", "date": datetime.datetime(2013, 1, 20, 12, 0)},
    {"name": "Nexus One", "date": datetime.datetime(2013, 1, 20, 13, 0)},
    {"name": "iPhone 14", "date": datetime.datetime(2013, 1, 20, 13, 30)},
    {"name": "Nexus One", "date": datetime.datetime(2013, 1, 20, 14, 0)},
    {"name": "iPhone 14", "date": datetime.datetime(2013, 1, 21, 15, 30)},
    {"name": "iPhone 14", "date": datetime.datetime(2013, 1, 21, 15, 40)},
    {"name": "Nexus One", "date": datetime.datetime(2013, 1, 21, 16, 20)},
    {"name": "iPhone 14", "date": datetime.datetime(2013, 1, 21, 17, 0)},
    {"name": "Nexus One", "date": datetime.datetime(2013, 1, 21, 18, 0)},
    {"name": "Nexus One", "date": datetime.datetime(2013, 1, 22, 19, 0)}
]

collection.insert_many(docs)