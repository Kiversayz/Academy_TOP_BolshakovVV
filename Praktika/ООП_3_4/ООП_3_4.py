""" Задание 1
Создайте класс Human, который будет содержать
информацию о человеке.
Спомощью механизма наследования, реализуйте класс
Builder (содержит информацию о строителе), класс Sailor
(содержит информацию о моряке), класс Pilot (содержит
информацию о летчике).
Каждый из классов должен содержать необходимые
для работы методы. """


class Human:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
    
    def get_firstName(self):
        return self.__firstName
    
    def get_lastName(self):
        return self.__lastName

class Builder(Human):
    def __init__(self, firstName, lastName, professia):
        super().__init__(firstName, lastName)
        self.__professia = professia
    
    def get_professia(self):
        return self.__professia

builder = Builder('Валерий','Большаков','Плиточник')

print(builder.get_firstName())
print(builder.get_lastName())
print(builder.get_professia())


""" Задание 2
Создайте класс Passport (паспорт), который будет
содержать паспортную информацию о гражданине заданной страны.
С помощью механизма наследования, реализуйте
класс ForeignPassport (загран.паспорт) производный от
Passport.
Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
заграничного паспорта.
Каждый из классов должен содержать необходимые
методы. """





""" Задание 3
Создать базовый класс «Животное» и производные
классы «Тигр», «Крокодил», «Кенгуру». С помощью конструктора установить имя каждого животного и его характеристики. Создайте для каждого класса необходимые
методы и поля. """