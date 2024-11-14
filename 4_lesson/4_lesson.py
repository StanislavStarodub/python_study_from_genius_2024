### Списки:
'''
1. **Робота із списками:**
   Завдання: Створіть список чисел. Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.
'''
num_list = [x for x in range(11)]
num_list.append(10)
num_list.insert(3, 20)
num_list.remove(10)
print(num_list)

'''
2. **Знаходження суми:**
   Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.
'''
num_list = [x for x in range(11)]
print(sum(num_list))

'''
3. **Подвійні значення:**
   Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.
'''
num_list = [x for x in range(11)]
print(num_list)
num_list = [x * 2 for x in num_list]
print(num_list)

### Кортежі:
'''
1. **Робота із кортежами:**
   Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин").
    Виведіть кожен елемент кортежу окремо.
'''
fruit_tuple = ('apple', 'banana', 'orange')
for item in fruit_tuple:
    print(item)
# or
print(fruit_tuple[0], fruit_tuple[1], fruit_tuple[2])
'''
2. **Об'єднання кортежів:**
   Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.
'''
first_number_tuple = (2, 3, 6, 7, 1)
second_number_tuple = (45, 11, 23, 15)
ext_tuple = first_number_tuple[:] + second_number_tuple[:]
print(ext_tuple)

'''
### Словники:
1. **Робота із словниками:**
   Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена (ім'я, вік, спорт, команда тощо).
    Виведіть цю інформацію на екран.
'''
my_favorite_athlete = {
    'name' : 'Messi',
    'age' : 35,
    'sport' : 'soccer',
    'FC' : 'US Nations',
    'scores' : 345
}
for key, value in my_favorite_athlete.items():
    print(f'{key}, {value}')

'''
2. **Оновлення словника:**
   Завдання: 
   Додайте до словника нового спортсмена.
'''
athlete_list = []
athlete_list.append(my_favorite_athlete)

Sheva = {
    'name' : 'Shevchenko',
    'age' : 42,
    'sport' : 'soccer',
    'FC' : 'Ukraine',
    'scores' : 288
}
athlete_list.append(Sheva)
print(athlete_list)

my_favorite_athlete.update(Sheva)
print(my_favorite_athlete)

'''
3. **Пошук значення:**
   Завдання: Створіть словник, що містить інформацію про країни та їх столиці. 
   Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).
'''
countries_capitals = {
    "Ukraine": "Kyiv",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid"
}
capital = input("Write country name: ")

print(countries_capitals.get(capital, "No such country"))
