import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Ryabokonn"]
collection = db["office_supplies_results"]

# Запросы
# 1. Результаты реализации указанного товара (например, Pen)
result_1 = collection.find({"product_name": "Pen"})
for doc in result_1:
    print(1, doc)

# 2. Результаты реализации товара по цене ниже средней
average_price_cursor = collection.aggregate([{"$group": {"_id": None, "avg_price": {"$avg": "$price"}}}])
average_price = next(average_price_cursor)["avg_price"]
result_2 = collection.find({"price": {"$lt": average_price}})
for doc in result_2:
    print(2, doc)

# 3. Результаты реализации товара в указанных магазинах (например, Store A и Store B)
result_3 = collection.find({"product_name": "Pen", "store_name": {"$in": ["Store A", "Store B"]}})
for doc in result_3:
    print(3, doc)

# 4. Только название магазина, наименование товара и цена товара
result_4 = collection.find({}, {"store_name": 1, "product_name": 1, "price": 1})
for doc in result_4:
    print(4, doc)

# 5. Все атрибуты с сортировкой по названию магазина
result_5 = collection.find().sort("store_name", pymongo.ASCENDING)
for doc in result_5:
    print(5, doc)
