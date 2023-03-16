# # try:except
# class MyException(Exception):
#     pass
#
#
# try:
#     sdsds
#     print(22 / 0)
#     raise MyException
# except NameError as err:
#     print(err)
# except MyException:
#     print('myException')
# except Exception as err:
#     print(err)
# finally:
#     print('finish')


# # generator\


# def gen(name):
#     for ch in name:
#         yield ch
#
#
# g = gen('Ivan')
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# # ////
# def gen1(n):
#     for i in range(n):
#         yield f'{i} - Team1'
#
#
# def gen2(n):
#     for i in range(n):
#         yield f'{i} - Team2'
#
#
# teams = [gen1(8), gen2(5)]
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


# # Отримання щоразу нової назви
# import uuid
#
#
# def generator_name_img():
#     pattern = '{}.jpeg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
#
# gen = generator_name_img()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# # менеджер контекст:
# try:
#     with open('lw4.txt', 'r') as file:
#         print(file.read())
# except Exception as err:
#     print(err)


# відкриття та запис бінарних данних: в даному випадку робим копію
# try:
#     with open('lw4.png', 'rb') as file:
#         with open('lesson4a.png', 'wb') as file2:
#             file2.write(file.read())
#
# except Exception as err:
#     print(err)

# # бібліотека pickle -- що завгодно переводить в бінарні дані
# import pickle
#
# user = {'name': 'Max', 'age': 25}
# try:
#     with open('my_user', 'wb') as file:
#         pickle.dump(user, file)
# except Exception as err:
#     print(err)
# try:
#     with open('my_user', 'rb') as file:
#         user = pickle.load(file)
#         print(user)
# except Exception as err:
#     print(err)


# # зберігання даних в json форматі
# import json
#
# user = {'name': 'Max', 'age': 25}
# try:
#     with open('my_user.json', 'w') as file:
#         json.dump(user, file)
# except Exception as err:
#     print(err)
#
# user = {'name': 'Max', 'age': 25}
# try:
#     with open('my_user.json', 'r') as file:
#         user = json.load(file)
#         print(user)
# except Exception as err:
#     print(err)

# _____

# # a = ['left', 200]
# a = ['top', 200]
#
# match a:
#     case 'left' | 'top' as action, value:
#         print(action, value)
#     case _:
#         print('not found')
#
# b = ['Ivan', 26, True]
# match b:
#     case 'Ivan' | 'Stepan' as action, v, True as s:
#         print(action, v, s)
#     case _:
#         print('NTF')
#
# user = {'name': 'Max', 'age': 25}
# match user:
#     case {'name': str(name), 'age': int(age)}:
#         print(f'name= {name}, age= {age}')
#     case _:
#         print('NF')
#
# user2 = {'name': 'Max2', 'age': 25}
# match user2:
#     case {'name': 'Max' as name, 'age': int(age)}:
#         print(f'name= {name}, age= {age}')
#     case _:
#         print('NF')

# _____
# # match into class
# class User:
#     __match_args__ = 'name', 'age'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user = User('Maxx', 25)
# user2 = {'name': 'Ivan', 'age': 27}
#
#
# def matcher(data: User | dict):
#     match data:
#         case User('Max' as name):
#             print(name)
#         case {'name': str(name)}:
#             print(name)
#         case _:
#             print('Nf')
#
#
# matcher(user)
# matcher(user2)
