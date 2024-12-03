""" Задание 8.1.1
Вам необходимо создать класс транспортное средство: Vehicle
Инициализируется класс следующими данными (их еще называют
поля или атрибуты класса):
Марка - name
Пробег - mileage
У класса есть следующие методы:
Определение типа ТС - get_vehicle_type(): в этот метод при его
вызове вы передаете количество колес, если их 2 то метод
возвращает что это мотоцикл, если 3 то метод возвращает что
это трицикл, если 4 то метод возвращает что это автомобиль,
если больше 4 то метод возвращает я не знаю таких ТС. Пример
возвращаемого сообщения:
Это мотоцикл марки BMW.
или
Это автомобиль марки Audi.
Метод который дает совет по приобретению
get_vehicle_advice(): который в зависимости от указанного при
инициализации пробега сообщает как к нему относиться:
- если пробег менее 50000 то вернет сообщение
"Неплохо (марка) можно брать."
- если пробег 50001 - 100000 то вернет сообщение
"(марка) надо внимательно проверить."
- если пробег 100001 - 150000 то вернет сообщение
"(марка) надо провести полную диагностику."
- если пробег более 150000 то вернет сообщение
"(марка) лучше не покупать."
Создать не менее 4х экземпляров класса с разными атрибутами
и проверить их по всем методам (как по количеству колес, так и
по пробегу. """


class Vehicle:

    def __init__(self, name, milaege):
        self.__name = name
        self.__milaege = milaege
    
    def get_vehicle_type(self,whell):
        self.__whell = whell
        if self.__whell  == 2:
            return f'Это мотоцикл'
        elif self.__whell  == 3:
            return f'Это трицикл'
        elif self.__whell  == 4:
            return f'Это автомобиль'
        else:
            return f'Я не знаю таких ТС'
        
    
    def get_vehicle_advice(self):
        if self.__milaege <=50000 :
            return f"Неплохо {self.__name} можно брать."
        elif 50000 < self.__milaege <= 100000:
            return f"{self.__name} надо внимательно проверить"
        elif 100000 < self.__milaege <= 150000:
            return f"{self.__name} надо провести полную диагностику."
        elif self.__milaege > 150000:
            return f"{self.__name} лучше не покупать."


vehicle_1 = Vehicle("LADA",149000)

print(vehicle_1.get_vehicle_advice())
print(vehicle_1.get_vehicle_type(1))
print()

vehicle_2 = Vehicle("Audi",9000)

print(vehicle_2.get_vehicle_advice())
print(vehicle_2.get_vehicle_type(2))
print()

vehicle_3 = Vehicle("Lexus",160000)

print(vehicle_3.get_vehicle_advice())
print(vehicle_3.get_vehicle_type(3))
print()

vehicle_4 = Vehicle("Jeep",53000)

print(vehicle_4.get_vehicle_advice())
print(vehicle_4.get_vehicle_type(4))
