import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Ryabokonn"]
collection = db["office_supplies_results"]

# Добавление документов
data = [
    {"store_name": "Store A", "product_name": "Pen", "incoming_quantity": 100, "sold_quantity": 80, "price": 1.5},
    {"store_name": "Store B", "product_name": "Notebook", "incoming_quantity": 50, "sold_quantity": 40, "price": 3.0},
    {"store_name": "Store A", "product_name": "Pencil", "incoming_quantity": 100, "sold_quantity": 80, "price": 1.7},
    {"store_name": "Store A", "product_name": "Glue", "incoming_quantity": 70, "sold_quantity": 10, "price": 1.3},
    {"store_name": "Store A", "product_name": "Stapler", "incoming_quantity": 60, "sold_quantity": 40, "price": 2.8},
    {"store_name": "Store A", "product_name": "Clipboard", "incoming_quantity": 100, "sold_quantity": 50, "price": 0.5},
    {"store_name": "Store A", "product_name": "Punch", "incoming_quantity": 40, "sold_quantity": 20, "price": 2.5},
    {"store_name": "Store A", "product_name": "Ruler", "incoming_quantity": 100, "sold_quantity": 70, "price": 4.5},
    {"store_name": "Store A", "product_name": "Envelope", "incoming_quantity": 120, "sold_quantity": 80, "price": 1.0},
    {"store_name": "Store A", "product_name": "Cutter", "incoming_quantity": 130, "sold_quantity": 60, "price": 1.5},
    {"store_name": "Store A", "product_name": "Paperclip", "incoming_quantity": 100, "sold_quantity": 80, "price": 1.5},
    {"store_name": "Store A", "product_name": "Scotch", "incoming_quantity": 50, "sold_quantity": 30, "price": 1.0},
    {"store_name": "Store A", "product_name": "Eraser", "incoming_quantity": 100, "sold_quantity": 30, "price": 1.5},
    {"store_name": "Store A", "product_name": "Calculator", "incoming_quantity": 150, "sold_quantity": 80, "price": 2.5},
    {"store_name": "Store A", "product_name": "Folder", "incoming_quantity": 20, "sold_quantity": 10, "price": 2.5},
    {"store_name": "Store A", "product_name": "File", "incoming_quantity": 100, "sold_quantity": 40, "price": 1.4},
    {"store_name": "Store A", "product_name": "Sticker", "incoming_quantity": 110, "sold_quantity": 80, "price": 1.0},
]

collection.insert_many(data)

