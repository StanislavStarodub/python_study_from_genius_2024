"""
Завдання 1: Виконання GET-запиту

Створіть Python-сценарій, який використовує бібліотеку requests (pip install requests) для виконання GET-запиту до
веб-ресурсу та виведення вмісту веб-сторінки на екран. Використовуйте функцію requests.get()
для виконання запиту.
"""
import requests

site = "https://jsonplaceholder.typicode.com/"

response = requests.get(url=site)
print(response)
print("_______________")

"""
Завдання 2: Параметри запиту
Розширте попереднє завдання, додаючи можливість вказати параметри запиту.
Виконайте GET-запит до веб-ресурсу, передаючи параметри запиту, такі як параметри запиту у URL
або параметри через словник.

Завдання 4: Обробка відповіді

Після виконання запиту, розпарсьте вміст HTTP-відповіді та виведіть потрібну інформацію.
 Наприклад, виведіть заголовки відповіді або вміст сторінки.
"""
site = "https://jsonplaceholder.typicode.com/posts"

"""
response = requests.get(url=site) # all posts
print(response.text)
print("_______________")
"""

response = requests.get(url=site + "/1") # only one post
print(response.json())
print("_______________")

print(response.json()['title'])
print("_______________")

# List of all headers and values on the site
for header, value in response.headers.items():
    print(f"Header: {header} --> Value: {value}")
    print("<_____________________>")

"""
Завдання 3: POST-запит

Створіть Python-сценарій для виконання POST-запиту до веб-ресурсу. Відправте дані на сервер,
 наприклад, форму з ім'ям користувача і паролем.
"""

print(response.text)
print("_______________")
body = {
    "UserId" : 111,
    "UserName" : "Ari",
    "password" : "secret"
}

headers = {
    "Content-Type" : "application/json; charset=utf-8"
}

post_message = requests.post(site, data=body, params=headers)

print(post_message.status_code)
print(post_message.reason)
print(post_message.text)

"""
Метод put заміняє весь вміст того запиту, що ми отримуємо. Наприклад

data = {
    "title" : "new title - put"
}
response_put = requests.put(url=site + "/1", data=data)
print(response_put.status_code)
print(response_put.reason)
print(response_put.text)

The output is: 

200
OK
{
  "title": "new title - put",
  "id": 1
}
Тобто запитуєми1й перший запис було зетерто
"""

""" 
Метод patch робить зміни точково


data = {
    "title" : "new title - put"
}
response_patch = requests.patch(url=site + "/1", data=data)
print(response_patch.status_code)
print(response_patch.reason)
print(response_patch.text)

The output is:

200
OK
{
  "userId": 1,
  "id": 1,
  "title": "new title - put",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
"""
"""
Видалення конкретного (нехай першого) посту


response_delete = requests.delete(url=site + "/1")
print(response_delete.status_code)
print(response_delete.reason)
print(response_delete.text)
"""

"""
Завдання 6: Збереження вмісту в файл

Розширте ваш код, щоб зберегти отриманий вміст веб-сторінки у файл. Використайте функціонал Python
 для роботи з файлами для збереження вмісту.
"""
try:
    post_message = requests.post(site, data=body, params=headers)

    print(post_message.status_code)
    print(post_message.reason)
    print(post_message.text)

except Exception as e:
    print(f"The post isn't worked. Exception is {e} ")

with open("my_post.txt", mode="w") as f:
    f.write(post_message.text)
