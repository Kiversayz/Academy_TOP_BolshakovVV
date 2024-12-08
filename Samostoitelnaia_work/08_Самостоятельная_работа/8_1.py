""" 
Задача 8.1
Используя понятие множественного наследования,
разработайте класс «Окружность, вписанная в квадрат».
Поля:
для окружности - радиус;
для квадрата - сторона.
Методы:
для окружности длина и площадь;
для квадрата сторона и площадь.

"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def ploshad(self):
        """Вычисление площади окружности."""
        return round(math.pi * self.radius ** 2,2)

    def dlinaCircle(self):
        """Вычисление длины окружности."""
        return round(2 * math.pi * self.radius,2) 

class Square:
    def __init__(self, side):
        self.side = side

    def ploshad(self):
        """Вычисление площади квадрата."""
        return self.side ** 2

class InscribedCircle(Circle, Square):
    def __init__(self, side):
        """Наследуем из других классов для вычеслений"""
        Circle.__init__(self, side / 2) # Радиус вписанной окружности равен половине стороны квадрата
        Square.__init__(self, side)

    def get_str(self):
        """Выводим принтом все возможные расчеты исходя из введеных данных"""
        return (f"Окружность, вписанная в квадрат:\n"
                f"Радиус окружности: {self.radius}\n"
                f"Сторона квадрата: {self.side}\n"
                f"Площадь окружности: {Circle.ploshad(self)}\n"
                f"Длина окружности: {self.dlinaCircle()}\n"
                f"Площадь квадрата: {Square.ploshad(self)}")


inscribed_circle = InscribedCircle(20)
print(inscribed_circle.get_str())