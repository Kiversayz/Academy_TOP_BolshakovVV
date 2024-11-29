""" Задание 3
Создайте класс «Страна». Необходимо хранить в
полях класса: название страны, название континента,
количество жителей в стране, телефонный код страны,
название столицы, название городов страны. 

Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса """


class Cantri:

    def __init__(self, name_strana,name_kontinent,ludi,kod_strani,name_stali,names_gorodov):
        self.name_strana = name_strana
        self.name_kontinent = name_kontinent
        self.ludi =ludi
        self.kod_strani = kod_strani
        self.name_stali = name_stali
        if not names_gorodov: 
            print('У вас нет городов, давайте добавим их:')
            self.names_gorodov = []
            addTrue = True #Лучше убрать данную логику в отдельный метод перед иницилизацией или же добавить как отдельный метод
            while addTrue:
                addCity = input('Наименование города: ')
                self.names_gorodov.append(addCity)
                addWho = input('Еще? (да/нет) ')
                if addWho.lower() == 'нет':
                    addTrue = False
                
        else:
            self.names_gorodov = list(names_gorodov)
        
    def get_data(self):
        data_str = f"""
        Континет: {self.name_kontinent}
        Страна: {self.name_strana}
        Телефон: {self.kod_strani}
        Столица страны: {self.name_stali}
        Города страны: {', '.join(self.names_gorodov)}
        """
        return data_str


object_a = Cantri('Россия','Азия/Евразия','3 млн.','+7','Москва')

print(object_a.get_data())






