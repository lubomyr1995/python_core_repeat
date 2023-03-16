"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціонала:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь-якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""
import json
from datetime import datetime
from typing import TypedDict

PurchaseType = TypedDict('PurchaseType', {id: int, 'name': str, 'price': int})


class Shopping:
    """
    Конструктор
    """

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__shopping_list: list[PurchaseType] = []
        self.__read_file()
        self.__id = self.__gen_id()

    def __show_all(self):
        """
        Метод для виведення списку всіх записів в записній книжці
        """
        print('Мої покупки: ')
        print('* ' * 10)
        if not self.__shopping_list:
            print('У вас немає ще покупок. Спочатку створіть покупку')
        for purchase in self.__shopping_list:
            print(f'{purchase["id"]}. {purchase["name"]} - {purchase["price"]}')
        print(' ')

    def __add(self):
        """
        Метод для створення нового запису в записній книжці
        """
        name = input('Введіть назву покупки: ')
        while True:
            try:
                price = int(input('Введіть ціну: '))
                break
            except (Exception,):
                pass
        self.__shopping_list.append({'id': int(datetime.timestamp(datetime.now())), 'name': name, 'price': price})
        self.__write_file()

    def __find_by(self):
        """
        Метод пошуку покупки
        """
        keys = ['id', 'name', 'cost']

        for i, v in enumerate(keys):
            print(f'{i}) {v}')

        choice = int(input("По чому будемо шукати: "))
        search = input("пошук: ")

        for item in self.__shopping_list:
            if str(item[keys[choice]]) == search:
                print(item)

    def __most_expensive_purchase(self):
        """
        Метод для визначення найдорожчої покупки.
        """
        if not self.__shopping_list:
            print('No purchases yet. You can add using the add() method.')
        else:
            print(max(self.__shopping_list, key=lambda i: i['price']))

    def __delete_by_id(self):
        """
        Метод видалення покупки по ідентифікатору
        """
        self.__show_all()
        _id = input("Введіть id: ")

        index = next((i for i, v in enumerate(self.__shopping_list) if str(v['id']) == _id), None)

        if index is not None:
            self.__shopping_list.pop(index)
            self.__write_file()
            return

        print("Error")

    def __read_file(self):
        """
        Метод читання файла
        """
        try:
            with open(self.__file_name) as file:
                self.__shopping_list = json.load(file)
        except (Exception,):
            self.__write_file()

    def __write_file(self):
        """
        Метод запису файла
        """
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__shopping_list, file)
        except Exception as err:
            print(err)

    @staticmethod
    def __gen_id():
        """
        Метод генерації ідентифікатора
        """
        id_ = 1
        while True:
            yield id_
            id_ += 1

    def menu(self):
        while True:
            print("1) вивід всіх покупок")
            print("2) додавати покупку в книгу")
            print("3) шукати по будь якому полю покупку")
            print("4) показати найдорожчу покупку")
            print("5) видаляти покупку по id")
            print("9) Вихід")
            choice = input("Зробіть свій вибір: ")
            print("*" * 50)

            match choice:
                case '1':
                    self.__show_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find_by()
                case '4':
                    self.__most_expensive_purchase()
                case '5':
                    self.__delete_by_id()
                case '9':
                    break


FILENAME = 'purchases.txt'
purchases = Shopping(FILENAME)
purchases.menu()
