# # EX1 Є файл email, записати в новий файл пошти в кого gmail.com
#
# file = 'emails.txt'
# new_file = 'emails_only_gmail.txt'
#
# try:
#     with open(file=file) as file, open(new_file, 'w') as new_file:
#         for line in file:
#             email = line.split()[-1]
#             print(email)
#             if email.endswith('@gmail.com'):
#                 # print(email, file=new_file)
#                 new_file.write(f'{email}\n')
#
# except Exception as err:
#     print(err)

"""
    Створити записну книжку покупок:
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

PurchaseType = TypedDict('PurchaseType', {id: int, 'purchase': str, 'price': int})

FILENAME = 'shopping_list.txt'


class Shopping:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__shopping_list: list[PurchaseType] = []

        try:
            with open(file_name) as file:
                self.__shopping_list = json.load(file)
        except:
            pass

    def add(self):
        """
        Функція для створення нової записі в записній книжці
        """
        try:
            with open(self.__file_name, 'w') as file:
                id_ = int(datetime.timestamp(datetime.now()))
                purchase = input('Input name purchase: ')
                price = int(input('Input price: '))
                self.__shopping_list.append({'id': id_, 'purchase': purchase, 'price': price})
                json.dump(self.__shopping_list, file)
        except Exception as err:
            print(err)

    def show_all(self):
        """
        Функція для виведення списку всіх записів в записній книжці
        """
        if not self.__shopping_list:
            print('No purchases yet. You can add using the add() method.')
        for i in self.__shopping_list:
            print(i)

    def summ_all_purchase(self):
        """
        Функція для виведення загальної ціни всіх покупок
        """
        if not self.__shopping_list:
            print('No purchases yet. You can add using the add() method.')
        else:
            sum_all = sum([i['price'] for i in self.__shopping_list])
            print(f'{sum_all=}')

    def most_expansive_purchase(self):
        """
        Функція для визначення найдорожчої покупки
        """
        if not self.__shopping_list:
            print('No purchases yet. You can add using the add() method.')
        else:
            print(max(self.__shopping_list, key=lambda i: i['price']))

    def search_purchase(self):
        """
        Функція для пошуку покупки
        :return:
        """
        find = input('Input name purchase')
        for i in self.__shopping_list:
            if i['purchase'].lower() == find.lower():
                print(i)
                return
        print('Not find!!!')


shopping = Shopping(FILENAME)
while True:
    print(20 * '-')
    print('1) Cтворити запис')
    print('2) Список всіх записів')
    print('3) Загальна сума всіх покупок')
    print('4) Найдорожча покупка покупка')
    print('5) Пошук за назвою покупки')
    print('9) Вихід')
    print(20 * '-')

    choice = input('Make your choice: ')
    match choice:
        case '1':
            shopping.add()
        case '2':
            shopping.show_all()
        case '3':
            shopping.summ_all_purchase()
        case '4':
            shopping.most_expansive_purchase()
        case '5':
            shopping.search_purchase()
        case '9':
            break
