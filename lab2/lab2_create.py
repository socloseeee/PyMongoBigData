import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Ryabokon"]
collection = db["office_supplies_results"]

# Добавление документов
data = [
    {"store_name": "Store A", "product_name": "Pen", "incoming_quantity": 100, "sold_quantity": 80, "price": 1.5},
    {"store_name": "Store B", "product_name": "Notebook", "incoming_quantity": 50, "sold_quantity": 40, "price": 3.0},
    # Добавьте больше документов здесь
]

collection.insert_many(data)

