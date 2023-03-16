# # 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# # - перший записує в список нову справу
# # - другий повертає всі записи
# def notebook():
#     todo_list = []
#
#     def add__todo(todo):
#         todo_list.append(todo)
#
#     def get__all():
#         return todo_list
#
#     return add__todo, get__all
#
#
# add_todo, get_all = notebook()
# add_todo('do1')
# add_todo('do2')
# add_todo('do3')
# add_todo('do4')
# add_todo('do5')
# print(get_all())

# # 2) протипізувати перше завдання
from typing import Callable, Tuple, List


def notebook() -> Tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add__todo(todo: str) -> None:
        todo_list.append(todo)

    def get__all() -> List[str]:
        nonlocal todo_list
        return todo_list

    return add__todo, get__all

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:

# # expanded_form(12) # return '10 + 2'
# # expanded_form(42) # return '40 + 2'
# # expanded_form(70304) # return '70000 + 300 + 4'
# def expanded_form(n: int) -> str:
#     st = str(n)
#     lst = []
#     for i, j in enumerate(st):
#         if j != '0':
#             lst.append(f'{j}{("0" * (len(st) - i - 1))}')
#     return '+'.join(lst)
#
#
# print(expanded_form(42))
# print(expanded_form(142))
# print(expanded_form(70304))
# print(expanded_form(1))

# # 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# # та буде виводити це значення після виконання функцій
# from typing import Callable
#
#
# def dec(f: Callable) -> Callable:
#     counter = 0
#
#     def inner() -> None:
#         nonlocal counter
#         f()
#         counter += 1
#         print('Викликів ф-ї: ', counter)
#
#     return inner
#
#
# @dec
# def say_hello() -> None:
#     print('Hello')
#
#
# say_hello()
# say_hello()
# say_hello()


# # # EX5 створити ф-ю на замикання яка буде повертати декоратор який буде рахувати
# # # загальну кількість запущених ф-ій декоровваних цим декоратором
# from typing import Callable
#
#
# def func_dec() -> Callable:
#     counter: dict = dict()
#
#     def dec(f: Callable) -> Callable:
#         nonlocal counter
#         counter[f] = 0
#
#         def inner() -> None:
#             counter[f] += 1
#             f()
#             print('COUNT: ', sum(counter.values()))
#             print(counter)
#             print('*' * 10)
#
#         return inner
#
#     return dec
#
#
# decorator = func_dec()
#
#
# @decorator
# def f1() -> None:
#     print('f1')
#
#
# @decorator
# def f2() -> None:
#     print('f2')
#
#
# f1()
# f1()
# f2()
# f1()
# f2()
