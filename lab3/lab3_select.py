from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Выбор базы данных
db = client['labb3']

# Выбор коллекции
collection_name = 'family'
collection = db[collection_name]

# Функция для вывода информации о документах
def print_documents(cursor):
    for document in cursor:
        print(document)

# 1. Добавление атрибута "страна проживания"
collection.update_many({}, {'$set': {'Страна проживания': 'Россия'}})
print('Действие 1: Добавлен атрибут "Страна проживания"')
print_documents(collection.find())

# 2. Удаление одного телефона из атрибут-массивов
collection.update_one({'Фамилия и инициалы': 'Иванов И.И.'}, {'$pop': {'Номер телефона': -1}})
print('Действие 2: Удален один телефон из атрибут-массива "Номер телефона"')
print_documents(collection.find())

# 3. Добавление номера телефона в атрибут-массив
collection.update_one({'Фамилия и инициалы': 'Иванов И.И.'}, {'$push': {'Номер телефона': '555555555'}})
print('Действие 3: Добавлен номер телефона в атрибут-массив "Номер телефона"')
print_documents(collection.find())

# 4. Изменение значения атрибута "город проживания"
collection.update_many({'Фамилия и инициалы': 'Иванов И.И.'}, {'$set': {'Город проживания': 'Санкт-Петербург'}})
print('Действие 4: Изменено значение атрибута "Город проживания"')
print_documents(collection.find())

# 5. Удаление документов с годом рождения, превышающим 1990
collection.delete_many({'Год рождения': {'$gt': 1990}})
print('Действие 5: Удалены документы с годом рождения, превышающим 1990')
print_documents(collection.find())

# Вывод количества оставшихся документов
print(f'Количество оставшихся документов: {collection.count_documents({})}')
