class Abiturient: #создаем класс - абитуриент

    def __init__(self, firstName, lastName, bals):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__bals = bals
    
    def get_bals (self): # для получения баллов
        return self.__bals
    
    def get_firstName (self): # для получения имени
        return self.__firstName 
    
    def get_lastName (self): # для получения фамилии
        return self.__lastName
    
    def get_lgots(self,lgots): # для подсчета баллов за льготы +10 баллов за каждый пункт
        self.__lgots = lgots
        for lgot in self.__lgots:
            self.__bals += 10
            if  self.__bals>100:
                self.__bals = 100
                #print(f'С учетом указанных льгот, у кандидата теперь максимальный уровень баллов = {self.__bals}.')
                return self.__bals
        #print(f'С учетом указанных льгот, у кандидата теперь {self.__bals} баллов.')
        return self.__bals

#аbiturient_1 = Abiturient('Валерий','Большаков',30)

#аbiturient_1_lgots = ['Инвалид первой степени','Сирота']

#аbiturient_1.get_lgots(аbiturient_1_lgots)

#print(аbiturient_1.get_bals())

abiturients = [ #список абитуриентов
{
    'firstName': 'Валерий' ,
    'lastName': 'Большаков',
    'bals': 47,
    'lgots': ['Чиновник']
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

def create_mass_class_abiturients (mass): # создание массива классов абитуриентов из списка абитуриентов
    newMass = []
    
    for id in mass:
        class_abiturient = Abiturient(firstName = id['firstName'] , lastName =id['lastName'] , bals = id['bals'])
        class_abiturient.get_lgots(id['lgots'])
        newMass.append(class_abiturient)
        #print(newMass)
    
    return newMass

mass_class_abiturients = create_mass_class_abiturients(abiturients) #сохраняем список классов абитуриентов

#print(mass_class_abiturients[0].get_bals())

def sorted_print_class_abiturients(mass_class_abiturients): # функция которая сортирует список абитуриентов и выводит принтом

    sorted_mass_class_abiturients = sorted(mass_class_abiturients, key=lambda abiturient: abiturient.get_bals(), reverse=True)

    #print(sorted_mass_class_abiturients[0].get_bals())

    len = 0

    for top in sorted_mass_class_abiturients:
        len+=1
        print(f'{len}. Кандидат {top.get_lastName()} {top.get_firstName()} набрал {top.get_bals()}' )
    
    print(f'В данном конкурсе выигрывает кандидат - {sorted_mass_class_abiturients[0].get_lastName()} {sorted_mass_class_abiturients[0].get_firstName()} набрав {sorted_mass_class_abiturients[0].get_bals()} балла.')
    
    return sorted_mass_class_abiturients

sorted_print_class_abiturients(mass_class_abiturients) #выводим принтом всех абитуриентов по ворядку и выводим победителя

