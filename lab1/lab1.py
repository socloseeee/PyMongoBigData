import pymongo

# Подключение к серверу MongoDB (может потребоваться указать адрес сервера)
client = pymongo.MongoClient()

# Создание базы данных и коллекции
db = client['exam_results']
collection = db['results']

# Добавление документов
data = [
    {
        'discipline': 'Математика',
        'teacher': 'Иванов Иван Иванович',
        'assessment_type': 'экзамен',
        'grade': 4
    },
    {
        'discipline': 'Физика',
        'teacher': 'Петров Петр Петрович',
        'assessment_type': 'зачет',
        'grade': 5
    },
    {
        'discipline': 'История',
        'teacher': 'Сидоров Сидор Сидорович',
        'assessment_type': 'экзамен',
        'grade': 3
    }
]

collection.insert_many(data)

# Вывод документов
for doc in collection.find({'assessment_type': 'экзамен'}):
    print(doc)