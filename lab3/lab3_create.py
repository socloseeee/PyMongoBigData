from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Создание или выбор базы данных
db = client['lab3']

# Создание коллекции
collection_name = 'family'
collection = db[collection_name]

# Документы для вставки
documents = [
    {
        'Фамилия и инициалы': 'Иванов И.И.',
        'Номер телефона': ['123456789', '987654321'],
        'Год рождения': 1990,
        'Город проживания': 'Москва',
        'Адрес': {
            'улица': 'Улица Пушкина',
            'номер дома': '10',
            'номер квартиры': '5'
        }
    },
]

# Вставка документов
result = collection.insert_many(documents)

print(f'{len(result.inserted_ids)} документов успешно добавлено в коллекцию "{collection_name}"')
