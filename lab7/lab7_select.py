from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Создание базы данных
db = client['university']

students_collection = db['students']

results_collection = db['exam_results']

# Получаем данные о студентах из коллекции
students_data = students_collection.find()

# Обновляем результаты сессии, добавляя поле "студент_id"
for student_data in students_data:
    student_name = student_data["ФИО"]
    result_data = results_collection.find_one({"ФИО": student_name})
    if result_data:
        result_id = result_data["_id"]
        student_id = student_data["_id"]
        results_collection.update_one({"_id": result_id}, {"$set": {"студент_id": student_id}})


# Вывод результатов
cursor = results_collection.find({}, {"_id": 0})
for result in cursor:
    print(result)

# Закрытие соединения с MongoDB
client.close()