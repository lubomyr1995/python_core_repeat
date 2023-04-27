class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """
            :return тут ми можемо повертати будь-що.
        """
        return f"Person(name='{self.name}')"
        # return {"type": "asasncjknascjkna"}

    def __str__(self):
        """
            :return тут ми не можемо повертати будь-що нариклад dict. Тут обовязково повертається стрінга
        """
        return f"Person name: {self.name}"


person = Person("IVAN")
"""
рядок нижче:
це візьме метод __str()__ самостійно) так як ми print використовуєм. А якщо str не буде а repr буде
тоді візьме за замовчуванням __repr()__. А якщо нічого не буде то отримаєм рядок представлення обєкта(абракадабру)
"""
print(person)
print(type(person))

print(type(person.__str__()))
print(person.__str__())

print(type(person.__repr__()))
print(person.__repr__())
