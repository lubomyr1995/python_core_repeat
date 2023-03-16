import os
import subprocess

"""
os - це стандартна бібліотека Python, яка надає функції для взаємодії з операційною системою.
Ця бібліотека містить методи для виконання різних операцій з файловою системою, управління процесами,
отримання та зміни поточної робочої директорії та багато іншого.

Деякі приклади функцій, що надає os:

os.uname() - показує про дану операційну систему
os.environ - показує всі змінні системи
os.system() - запуск команд через пайтон, але цю команду потрібно запускати від імені адміністратора:
sudo python3 /Users/lubomyr/Desktop/okten-repeat/python/python_core/library_os/os_test.py
os.getcwd() - повертає поточну робочу директорію.
os.mkdir() -створення папок
os.os.path.join() - робить шлях з того що ми прописуєм в join(), тобто ставить слеші до відповідної операційки
os.walk() - вміє рекурсивно ходити по всій структурі папок
os.listdir(path) - повертає список файлів та папок вказаної директорії.
os.makedirs(name) - створює директорію зі зазначеною назвою.
os.remove(path) - видаляє файл зі зазначеним шляхом.
os.rename(src, dst) - перейменовує файл або директорію.
os - це дуже корисна бібліотека для роботи з файловою системою, тому що вона дозволяє взаємодіяти з 
операційною системою безпосередньо з Python. Використовуючи функції os, ви можете автоматизувати багато 
рутинних завдань, пов'язаних з управлінням файлами та директоріями, зменшивши кількість ручної роботи.
"""

# print(os.uname())
# print(os.environ)
# os.system('htop')
# os.getcwd()
# path_join = os.path.join('second', 'first', 'file.txt')
# print(path_join)
print(list(os.walk('.')))
