from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Создание базы данных
db = client['university2']

students_collection = db['students']

results_collection = db['exam_results']

# Получаем данные о студентах из коллекции
results_data = results_collection.find()

# Обновляем результаты сессии, добавляя поле "студент_id"
for result_data in results_data:
    student_data = students_collection.find_one({"ФИО": result_data["ФИО"]})
    result_id = result_data["_id"]
    student_id = student_data["_id"]
    results_collection.update_one(
        {"_id": result_id},
        {"$set": {"студент_id": {"$db": "university", "$ref": "students", "$id": student_id}}}
    )
    """$db: Этот атрибут указывает на имя базы данных"""
    """$ref: Этот атрибут определяет коллекцию, к которой относится ссылочный документ"""
    """$id: Этот атрибут определяет идентификатор ссылочного документа в коллекции"""

# Вывод результатов
cursor = results_collection.find({}, {"_id": 0})
for result in cursor:
    print(result)

# Закрытие соединения с MongoDB
client.close()
