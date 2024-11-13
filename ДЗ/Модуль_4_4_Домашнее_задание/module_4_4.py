

""" #Тесты с аргс и кваргс
def test_args_kwargs (*args, **kwargs):
    print(f'Длина поступишего Аргса: {len(args)}')
    print(f'Длина поступишего Кваргса: {len(kwargs)}')
    for arg in args:
        print(f"Привет, {arg}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#test_args_kwargs("Влерий", "Анатолий", "Дедушка", age=30, city="Набережные челны")

print() """

argsNames = ["Влерий", "Анатолий", "Моцарт","Боб"]
argsAges = ['15','20','30','60']
argsCitys = ['Набережные челны','Казань','Москва','Нижнекамск']
argsFriend = ["Дедушка",'Призедент','Питтца',"Чайка"]

kwargs = {'Имя':'','Возраст': '', 'Город':'','Друг':''}

#test_args_kwargs(*argsNames,*argsAges,*argsCitys,*argsFriend,**kwargs) #может принимать и переменные если еказать *

def gluing_args_kwargs (*args, **kwargs):
    """Данная функция позваляет создать список словарей,
    передавайте [список] к первому заготовленному {Словарю} для наполнения
    и кол-во аргументов должно быть в соответсвии с кол-во словаря.
    В результате получим список словорей.
    Пример: [Имя], [Возраст], [Город], [Друг], {Словарь}"""
    print(f'Длина поступишего Аргса: {len(args)}')
    print(f'Длина поступишего Кваргса: {len(kwargs)}')
    
    container = []
    
    if len(args)%len(kwargs)==0:
        for step in range(0,len(kwargs)):
            step_arg = step
            container.append({})
            for key, value in kwargs.items():
                container[step][key] = args[step_arg]
                step_arg+=len(kwargs)
            print(f"{container[step]}")
    else:
        return print(f'Колличество Аргументов не совпадает с кол-вом Словоря')
    return container

gluing_args_kwargs(*argsNames,*argsAges,*argsCitys,*argsFriend,**kwargs)



