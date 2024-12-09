""" 
Задача 8.2
Используя механизм множественного наследования или
композицию разработайте класс “Автомобиль”. Должны быть
классы «Колеса», «Двигатель», «Двери». Требования к классам:
2 поля (атрибута) - они должны быть защищены
ко всем полям написаны геттеры
к 1 полю написан еще и сеттер
"""

class Wheel:
    
    def __init__(self, nameWheel, radius):
        self.__nameWheel = nameWheel #название фирмы колеса
        self.__radius = radius #радиус колеса
    
    def get_nameWheel(self):
        """Вернем название фирмы колеса"""
        return self.__nameWheel
    
    def get_radius(self):
        """Вернем радиус колеса"""
        return self.__radius
    
    def set_radius(self,radius):
        """Устанавливаем и название фирмы колеса"""
        self.__radius = radius
        return self.__radius

class Engine:
    
    def __init__(self, typeEngine, power):
        self.__typeEngine = typeEngine #тип двигателя
        self.__power = power #Мощьность двигателя
    
    def get_typeEngine(self):
        """Вернем тип двигателя"""
        return self.__typeEngine
    
    def get_power(self):
        """Вернем мощьность двигателя"""
        return self.__power
    
    def set_power(self,power):
        """Устанавливаем и Вернем мощьность двигателя"""
        self.__power = power
        return self.__power

class Door:
    
    def __init__(self, typeDoor, thickness):
        self.__typeDoor = typeDoor #Тип двери По способу открывания
        self.__thickness = thickness #Толщина материала
    
    def get_typeDoor(self):
        """Вернем название Тип двери По способу открывания"""
        return self.__typeDoor
    
    def get_thickness(self):
        """Вернем Толщину материала"""
        return self.__thickness
    
    def set_thickness(self,thickness):
        """Устанавливаем и Вернем Толщину материала"""
        self.__thickness = thickness
        return self.__thickness

class Auto(Wheel, Engine, Door):
    def __init__(self, nameWheel, radius, typeEngine, power, typeDoor, thickness, modelAuto, markaAuto):
        Wheel.__init__(self, nameWheel, radius) # Вызов конструктора Wheel
        Engine.__init__(self, typeEngine, power) # Вызов конструктора Engine
        Door.__init__(self, typeDoor, thickness) # Вызов конструктора Door
        self.__modelAuto = modelAuto #Модель автомобиля
        self.__markaAuto = markaAuto #Марка автомобиля
    
    def get_str_auto(self):
        return (f"Характиристики Автомобиля:\n"
                f"Марка автомобиля: {self.__markaAuto}\n"
                f"Модель автомобиля: {self.__modelAuto}\n"
                f"Тип двери по способу открывания: {Door.get_typeDoor(self)}\n"
                f"Толщина материала двери: {Door.get_thickness(self)}\n"
                f"Тип двигателя: {Engine.get_typeEngine(self)}"
                f"Мощьность двигателя (л.с.): {Engine.get_power(self)}\n"
                f"Название фирмы колеса: {Wheel.get_nameWheel(self)}\n"
                f"Радиус колеса: {Wheel.get_radius(self)}\n")

auto_1 = Auto('Dunlop', 16, 'Бензиновый', 150, 'ножницы',0.8,'2170','LADA')

print(auto_1.get_str_auto())

auto_1.set_power(250) #увеличиваем мощь авто
auto_1.set_radius(18) #увеличили радиус колес
auto_1.set_thickness(1.2) #накрасили еще один слой краски

print(auto_1.get_str_auto())