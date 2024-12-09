""" 
Создать базовый класс «Домашнее животное» и производные
классы «Собака», «Кошка», «Попугай», «Хомяк». С помощью
конструктора установить имя каждого животного и его
характеристики. Реализуйте для каждого из классов методы:
get_sound — издает звук животного (пишем текстом в
консоль);
get_name — отображает имя животного;
get_type — отображает название его подвида;
Поля у классов должны быть такие чтобы их можно корректно
было передать в методы также поля должны быть
защищены.
"""
class homeAnimals:
    
    def __init__(self,nameAnimal,typeAnimal):
        self.__nameAnimal = nameAnimal
        self.__typeAnimal = typeAnimal
    
    def get_nameAnimal(self):
        return self.__nameAnimal
    
    def get_typeAnimal(self):
        return self.__typeAnimal

class Animal(homeAnimals):
    
    def __init__(self,nameAnimal,typeAnimal,song):
        super().__init__(nameAnimal,typeAnimal)
        self.__song = song
    
    def get_songAnimal(self):
        print(self.__song)
        return self.__song

dog = Animal('Шарик', 'Собака','Гав-Гав')
dog.get_songAnimal()

cat = Animal('Крыся', 'Кошка','Мяу-мяу')
cat.get_songAnimal()

parrot = Animal('Каспер', 'Попугай','Каспер-дурак')
parrot.get_songAnimal()

hamster = Animal('Петр', 'Хомяк','Тап-Тап криптокойны')
hamster.get_songAnimal()