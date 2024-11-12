"""
Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`.
Використовуйте умовні конструкції і цикли для розв'язання кожного завдання.
"""

### Умовні конструкції:
"""
1. **Перевірка паролю:**
   Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє,
   чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123",
   виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
"""
correct_password = "password123"
user_input_password = "my_password" # замість = input("Введіть свій пароль")
if user_input_password == user_input_password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

"""
2. **Визначення днів тижня:**
   Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня.
   Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
"""
day_in_week = {
1 : "Понеділок",
2 : "Вівторок",
3 : "Середа",
4 : "Четвер",
5 : "П'ятниця",
6 : "Субота",
7 : "Неділя",
}
num_of_day = 9 # замість = int(input("Введіть номер дня тижня"))
if num_of_day:
    print(day_in_week.get(num_of_day, "Немає такого дня"))

### Цикли:
"""
1. **Таблиця множення:**
   Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
"""
entered_num = 2 # замість = int(input("Введіть число для отримання таблиці множення"))
for num in range(1, 11):
    res = entered_num * num
    print(f"{entered_num} * {num} = {res}")

"""
2. **Сума чисел:**
   Завдання: Визначте список чисел і обчисліть їх суму.
"""
num_list = [1, 3, 7, 2, 10, 5]
sum = 0
for num in num_list:
    sum+=num
print(f"The suma of the list is {sum}")
"""
3. **Факторіал числа:**
   Завдання: Обчисліть факторіал заданого числа.
"""
num_for_fact = 5
fact = 1
for num in range(2, num_for_fact + 1):
    fact *= num
print(f"The factorial of the number {num_for_fact} is {fact}")

"""
4. **Парні числа:**
   Завдання: Виведіть всі парні числа від 1 до 50.
"""
for num in range(1, 51):
    if num % 2 == 0:
        print(num)

"""
5. **Пошук простих чисел:**
   Завдання: Знайдіть всі прості числа в заданому діапазоні.
"""
end_off_range = 20 # замість = int(input("Введіть число для кінця діапазону"))

for num in range(1, end_off_range + 1):
    is_prime = True
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
