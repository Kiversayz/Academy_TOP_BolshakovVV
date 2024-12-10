""" Задача 8.4
Создать базовый класс Employer (служащий) с методом print(). 
Она должна выводить и информацию о служащем. 
В случае базового класса это может быть строка c надписью This is class, 
опционально можете добавить поля, 
которые бы как-то характеризовали ваш имя, фамилия, возраст) - вам пригодится в задании 8.5.
Создайте от него три производных класса: President, Manager, Worker. 
Переопределите функцию Print() для вывода информации, соответствующей каждому типу служащего. """





class Employer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print("This is class")
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Возраст: {self.age}")

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}"

    def __int__(self):
        return self.age

class President(Employer):
    def print_info(self):
        print("President Info:")
        super().print_info()

class Manager(Employer):
    def print_info(self):
        print("Manager Info:")
        super().print_info()

class Worker(Employer):
    def print_info(self):
        print("Worker Info:")
        super().print_info()

# Пример использования
president = President("Валерий", "Большаков", 27)
manager = Manager("Анатолий", "Антонов", 35)
worker = Worker("Борис", "Бритва", 25)

president.print_info()
print()

manager.print_info()
print()

worker.print_info()
print()

print(str(president))
print(int(president))