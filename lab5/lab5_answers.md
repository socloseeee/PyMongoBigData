1)Приведите синтаксис «$push» и «$pop»:
* $push: Добавляет элемент в конец массива.

```javascript
db.collection.update(query, { $push: { field: value } })
```

* $pop: Удаляет элемент из конца или начала массива.

```javascript
db.collection.update(query, { $pop: { field: 1 } }) // Удаляет последний элемент массива
db.collection.update(query, { $pop: { field: -1 } }) // Удаляет первый элемент массива
```

2)Каким образом можно вставить в массив несколько элементов? Приведите пример запроса:
Для вставки нескольких элементов в массив можно использовать оператор $push вместе с модификатором $each.

```
javascript
db.collection.update(query, { $push: { field: { $each: [value1, value2, ...] } } })
```

3)Для чего используются модификаторы массивов в запросах?
Модификаторы массивов в запросах MongoDB используются для изменения и обновления полей массивов в документах коллекции. Они позволяют добавлять, удалять, обновлять элементы массивов в соответствии с заданными критериями.

4)Какие способы обновления данных в массиве вы знаете? Приведите примеры:

* $push: Добавляет элемент в массив.

```javascript
db.collection.update(query, { $push: { field: value } })
```

* $pop: Удаляет элемент из массива.

```javascript
db.collection.update(query, { $pop: { field: 1 } }) // Удаляет последний элемент массива
```

* $addToSet: Добавляет элемент в массив, если его там еще нет.

```javascript
db.collection.update(query, { $addToSet: { field: value } })
```

* $pull: Удаляет все вхождения элемента из массива.

```javascript
db.collection.update(query, { $pull: { field: value } })
```