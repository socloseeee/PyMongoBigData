from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('localhost', 27017)

# Создание или выбор базы данных
db = client['art_gallery']

# Создание коллекции
collection_name = 'paintings'
collection = db[collection_name]

# Данные для вставки в коллекцию
data = [
    {
        'Фамилия и инициалы': 'Перов В.Г.',
        'Страна': 'Россия',
        'Год рождения': 1834,
        'Картины': ['Рыболов'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Саврасов А.К.',
        'Страна': 'Россия',
        'Год рождения': 1830,
        'Картины': ['Грачи прилетели', 'Поселок'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Шишкин И.И.',
        'Страна': 'Россия',
        'Год рождения': 1832,
        'Картины': ['Рожь', 'Осенний лес'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Репин И.Е.',
        'Страна': 'Россия',
        'Год рождения': 1844,
        'Картины': ['Диоген и мальчик'],
        'Техника рисования': ['Картон, масло']
    },
    {
        'Фамилия и инициалы': 'Поленов В.Д.',
        'Страна': 'Россия',
        'Год рождения': 1844,
        'Картины': ['Деревня Окулова гора'],
        'Техника рисования': ['Картон, масло']
    },
    {
        'Фамилия и инициалы': 'Васнецов В.М.',
        'Страна': 'Россия',
        'Год рождения': 1848,
        'Картины': ['Жница', 'Автопортрет'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Суриков В.И.',
        'Страна': 'Россия',
        'Год рождения': 1848,
        'Картины': ['Боярыня Морозова'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Ван Гог',
        'Страна': 'Голландия',
        'Год рождения': 1853,
        'Картины': ['Звездная ночь'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Мане Э.',
        'Страна': 'Франция',
        'Год рождения': 1832,
        'Картины': ['Флейтист'],
        'Техника рисования': ['Холст, масло']
    },
    {
        'Фамилия и инициалы': 'Сезан П.',
        'Страна': 'Франция',
        'Год рождения': 1839,
        'Картины': ['Мальчик в красном жилете'],
        'Техника рисования': ['Холст, масло']
    }
]

# Вставка данных в коллекцию
collection.insert_many(data)