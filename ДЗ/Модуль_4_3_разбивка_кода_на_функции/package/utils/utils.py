#Код разбитый на функции

def get_reg_data():
    return {
        'login':'',
        'pas':'',
        'email':'',
        'numbber':''
        }


def reg_users_data(users_massiv, raund):
    """ функция для проверки введенных
данных, принимает данные от пользователя, необходимый
паттерн для проверки, список уже созданных пользователей
(необходимо для проверки уникальности телефона и email)
возвращает user_data если были пройдены все проверки """
    for i in range(0,int(raund)):
        users_massiv.append(get_reg_data())
        
        users_massiv[i]['login'] = create_data_user (users_massiv, i, 'login')

        while users_massiv[i]['pas']=='':
            users_massiv[i]['pas'] = input('Введите пароль: ')
            if len(users_massiv[i]['pas']) < 6:
                users_massiv[i]['pas'] = ''
                print(f'Введите пожалуйста пароль не короче шести символов.')
        
        users_massiv[i]['email'] = create_data_user (users_massiv, i, 'email')
        
        users_massiv[i]['numbber'] = create_data_user (users_massiv, i, 'numbber')
        
        print(users_massiv)
    return users_massiv

def create_data_user (users, id, chek_kay):
    chek = True
    while chek:
        users[id][chek_kay] = input(f'Введите {chek_kay}: ')
        chek = check_unique_data(users, id, chek_kay)
    return users[id][chek_kay]

def check_unique_data(users, id, chek_kay):
    """ функция
для проверки уникальности введенных данных (номер
телефона и email) принимает данные которые ввел
пользователь и данные которые нужно проверить (уже
введенные номера телефонов и email). Она возвращает
булево значение. Её необходимо встроить в функцию def
reg_check """
    chek_id = users[id][chek_kay]
    point = 0
    for j in users:
            if j[chek_kay] == chek_id:
                point +=1
                if point>=2:
                    print('Значение уже есть у другого пользователя, введите другое.\n')
                    return True
    return False