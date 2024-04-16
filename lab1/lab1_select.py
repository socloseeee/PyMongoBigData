import pymongo

# Подключение к серверу MongoDB (может потребоваться указать адрес сервера)
client = pymongo.MongoClient()

# Создание базы данных и коллекции
db = client['exam_results']
collection = db['results']

# Вывод документов
for doc in collection.find({'assessment_type': 'экзамен'}):
    print(doc)