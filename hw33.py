# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

# class Rectangle:
#     def __init__(self, x: int, y: int):
#         self.y = y
#         self.x = x
#         self.area = x * y
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __len__(self):
#         return self.x * 2 + self.y * 2
#
#
# res1 = Rectangle(10, 10)
# res2 = Rectangle(20, 20)
#
# print(res1 + res2)
# print(res2 - res1)
# print(res1 == res2)
# print(res1 != res2)
# print(res1 < res2)
# print(res1 > res2)
# print(len(res1))
# print(len(res2))

# # створити класс Human (name, age)
# # створити два класси Prince и Cinderella які наслідуються від Human:
# # у попелюшки мае бути ім'я, вік, розмір нонги
# # у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде
# # приймати список попелюшок, та шукати ту саму
# #
# # в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# # також має бути метод классу який буде виводити це значення
#
# class Human:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
#     def __str__(self) -> str:
#         return str(self.__dict__)
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name: str, age: int, foot_size: int) -> None:
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.__count += 1
#
#     @classmethod
#     def get_count(cls) -> int:
#         return cls.__count
#
#
# class Prince(Human):
#     def __init__(self, name: str, age: int, find_foot_size: int) -> None:
#         super().__init__(name, age)
#         self.find_foot_size = find_foot_size
#
#     def find_cinderella(self, cds: list[Cinderella]) -> Cinderella | None:
#         for cinderella in cds:
#             if self.find_foot_size == cinderella.foot_size:
#                 return cinderella
#         return None
#
#
# prince = Prince('Ivan', 30, 36)
# cinderellas = [Cinderella('Kira', 22, 39), Cinderella('Vika', 22, 37), Cinderella('Ira', 22, 36),
#                Cinderella('Yulia', 22, 35)]
#
# print('prince: ', prince)
# print('cinderellas: ', cinderellas)
# print(prince.find_cinderella(cinderellas))
# print('count_cinderellas: ', Cinderella.get_count())


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        print('Printable')


class Book(Printable):
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__class__.__name__, self.__name)


class Magazine(Printable):
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__class__.__name__, self.__name)


class Main:
    __printable_list: list[Book | Magazine] = []

    @classmethod
    def add(cls, item: Magazine | Book) -> None:
        if isinstance(item, (Magazine, Book)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_books(cls) -> None:
        for book in cls.__printable_list:
            if isinstance(book, Book):
                book.print()

    @classmethod
    def show_all_magazines(cls) -> None:
        for magazine in cls.__printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
