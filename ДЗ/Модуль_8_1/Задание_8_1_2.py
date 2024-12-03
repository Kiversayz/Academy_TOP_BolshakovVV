class Abiturient:

    def __init__(self, firstName, lastName, bals):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__bals = bals
    
    def get_bals (self):
        return self.__bals
    
    def get_firstName (self):
        return self.__firstName 
    
    def get_lastName (self):
        return self.__lastName
    
    def get_lgots(self,lgots):
        self.__lgots = lgots
        for lgot in self.__lgots:
            self.__bals += 10
            if  self.__bals>100:
                self.__bals = 100
                print(f'С учетом указанных льгот, у кандидата теперь максимальный уровень баллов = {self.__bals}.')
                return self.__bals
        print(f'С учетом указанных льгот, у кандидата теперь {self.__bals} баллов.')
        return self.__bals

аbiturient_1 = Abiturient('Валерий','Большаков',30)

аbiturient_1_lgots = ['Инвалид первой степени','Сирота']

аbiturient_1.get_lgots(аbiturient_1_lgots)

print(аbiturient_1.get_bals())

abiturients = [
{
    'firstName': 'Валерий' ,
    'lastName': 'Большаков',
    'bals': 47,
    'lgots': []
},
{
    'firstName': 'Данил' ,
    'lastName': 'Саммигулин',
    'bals': 33,
    'lgots': ['Сирота','Отец одиночка','Герой войны','Ребенок инвалид']
},
{
    'firstName': 'Петр' ,
    'lastName': 'Петров',
    'bals': 95,
    'lgots': []
}
]

""" def create_mass_class_abiturients (mass):
    newMass = []
    
    for id in mass:
        class_abiturient = Abiturient(firstName = id[firstName] , lastName =id[lastName] , bals = id[bals])
        newMass.append(class_abiturient)
    
    return newMass """
