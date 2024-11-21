"""
Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)

Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP.
В цьому класі повинні бути методи для створення користувача, оновлення даних користувача
та видалення користувача. Переконайтеся, що кожен метод відповідає за одну конкретну функцію.
"""
class User:
    def __init__(self):
        self.users = []

    def __str__(self):
        return "\n".join(self.users)

    def create_user(self, name):
        if name not in self.users:
            self.users.append(name)
            print(f"The user {name} is created!")
            print("<------------->")
        else:
            print(f"The username {name} is alredy existed")

    def update_user_name(self, old_name, new_name):
        if old_name in self.users:
            index = self.users.index(old_name)
            print(f"The old list of users: {self.users}")
            self.users.insert(index, new_name)
            self.users.remove(old_name)
            print(f"The username {old_name} is renamed by username {new_name}")
            print(f"The updated list of users: {self.users}")
        else:
            print(f"The name {old_name} isn't in the list of names. You should call the create_user method.")

    def remove_user(self, name):
        if name in self.users:
            self.users.remove(name)
            print(f"The username {name} is removed!")
            print(f"The updated list of users: {self.users}")
        else:
            print(f"The name {name} isn't in the list of names.")

my_user_list=User()
wish_list = ['Vanya', 'Fedya', 'Sergey', 'Stas', 'Jhon', 'Ari']
for name in wish_list:
    my_user_list.create_user(name)

print(f"Count of users:\n{my_user_list}")

my_user_list.update_user_name('Fedya', 'Masha')
my_user_list.update_user_name('Masha111', 'Masha222')
my_user_list.remove_user('Masha')

