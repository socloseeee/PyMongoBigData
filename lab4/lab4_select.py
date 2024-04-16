from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Создание или выбор базы данных
db = client['art_gallery']

# Создание коллекции
collection_name = 'paintings'
collection = db[collection_name]

# Операция фильтрации российских авторов
russian_artists = collection.find({'Страна': 'Россия'})

# Разворачивание массива названий картины
for artist in russian_artists:
    paintings = artist['Картины']
    print(f"Фамилия и инициалы: {artist['Фамилия и инициалы']}, Картины: {', '.join(paintings)}")

# Группировка документов по технике рисования
pipeline = [
    {"$unwind": "$Техника рисования"},
    {"$group": {"_id": "$Техника рисования", "count": {"$sum": 1}}}
]

techniques_grouped = collection.aggregate(pipeline)

# Вывод результатов группировки
print("\nГруппировка по технике рисования:")
for item in techniques_grouped:
    print(f"{item['_id']}: {item['count']}")

# Закрываем соединение с базой данных
client.close()
