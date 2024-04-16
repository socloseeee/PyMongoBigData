from pymongo import MongoClient
from bson.code import Code


# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Выбор базы данных
db = client['test']

# 1. Создание коллекции и добавление документов
collection = db['selling']

# 3. Обработка коллекции с использованием MapReduce
mapper = Code("""
function () {
    emit(this.name, 1);
}
""")

reducer = Code("""
function (key, values) {
    return Array.sum(values);
}
""")

result = db.command({
    'mapreduce': 'selling',
    'map': mapper,
    'reduce': reducer,
    'out': 'selling_count'
})

# Вывод результата
for doc in db['selling_count'].find():
    print(doc)

# Закрытие соединения с MongoDB
client.close()

