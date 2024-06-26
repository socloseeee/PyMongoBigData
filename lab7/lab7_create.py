from pymongo import MongoClient
from bson import ObjectId

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Создание базы данных
db = client['university2']

# Создание коллекции для анкетных данных студентов
students_collection = db['students']

# Добавление документов с анкетными данными студентов
students_data = [
    {"_id": ObjectId(), "ФИО": "Иванов И.И.", "Пол": "М", "Возраст": 20, "Телефон": "+7 (123) 456-7890", "Семейное положение": "Холост"},
    {"_id": ObjectId(), "ФИО": "Петров П.П.", "Пол": "М", "Возраст": 22, "Телефон": "+7 (234) 567-8901", "Семейное положение": "Женат"},
    {"_id": ObjectId(), "ФИО": "Сидорова Е.В.", "Пол": "Ж", "Возраст": 21, "Телефон": "+7 (345) 678-9012", "Семейное положение": "Холост"},
]

# Вставка документов в коллекцию студентов
students_collection.insert_many(students_data)

# Создание коллекции для результатов сессии
results_collection = db['exam_results']

# Добавление документов с результатами сессии студентов
results_data = [
    {"_id": ObjectId(), "ФИО": "Иванов И.И.", "Предмет": "Математика", "Оценка": 4},
    {"_id": ObjectId(), "ФИО": "Петров П.П.", "Предмет": "Математика", "Оценка": 5},
    {"_id": ObjectId(), "ФИО": "Сидорова Е.В.", "Предмет": "Математика", "Оценка": 3},
]

# Вставка документов в коллекцию результатов сессии
results_collection.insert_many(results_data)