""" 
Шаг 5 (разбить код на функции)
Ваша программа уже существует и выполняет свою задачу, но пора
улучшить данный код разбив его на функции, ведь например выбор
сложности или градацию оценки можно применять не только для этого
теста!
Для этого ваш код необходимо распределить по трем функциям:
1) get_user_level - получает желаемый уровень от пользователя и
возвращает нам словарь в котором содержаться вопросы исходя
из уровня сложности (ввод уровня сложности просто в основном коде
не пихайте его в функцию, получили ввод - передали в функцию).
2) base_program - функция на входе получает список слов в
зависимости от сложности (да это результат работы get_user_level),
задает вопросы получает ответы добавляя их в словарь answers где
ключом является слов на английском а его значением True или False.
Функция возвращает словарь answers
Функция для того чтобы задавать вопросы использует:
input("Текст вопроса такой же как и был")
3) get_result - принимает на вход словарь с результатами ответов и
словарь уровня знаний, при помощи print() выводит правильно и
неправильно отвеченные слова, и возвращает показатель уровня
знаний согласно словаря.
4) Печатаем результат пользователя согласно результата работы
функции get_result
Вот как у меня выглядит основной код программы (то есть после
задания базовых значений и написания функций)
user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный.\n").lower()
test_words = функция
test_answers = функция
result = функция
print(f"\nВаш ранг:\n{result}")
Также структура проекта такая:
словари базовые (шаг 0)
функции (шаг 5)
основной код (шаг 5 черным шрифтом)
"""
import dz_5_1_Шаг_0 as glossary
import json
import os

def fun_1 ():
    print('Раздел с функциями работает!')

def get_user_level (difficulty_level = str()):
    """Запрашиваем желаемый уровень от пользователя и
    возвращает нам словарь в котором содержаться вопросы исходя
    из уровня сложности """
    
    level = difficulty_level
    
    if difficulty_level.lower() == 'легкий': 
        print('Отлично, уровень сложности - легкий')
        return glossary.words_easy
    
    elif difficulty_level.lower() == 'средний': 
        print('Отлично, уровень сложности - средний')
        return glossary.words_medium
    
    elif difficulty_level.lower() == 'тяжелый': 
        print('Отлично, уровень сложности - тяжелый')
        return glossary.words_hard
    
    else: 
        print(f'Мы не нашли совпадений, в этом случае уровень сложности - легкий')
        return glossary.words_easy



def base_program(words):
    """функция на входе получает список слов в
    зависимости от сложности (да это результат работы get_user_level),
    задает вопросы получает ответы добавляя их в словарь answers где
    ключом является слов на английском а его значением True или False.
    Функция возвращает словарь answers
    Функция для того чтобы задавать вопросы использует:
    input("Текст вопроса такой же как и был")"""
    
    answers = {}
    
    for translation, word in words.items():
        print(f'{translation}, {len(word)} букв, начинается на {word[0]}...')
        answer = input('Введите перевод слова целиком: ')
        if str(answer).lower() == str(word).lower():
            answers[translation] = True
            print(f'Верно, {translation} — это {word}.')
            print()
        else:
            answers[translation] = False
            print(f'Неверно, {translation} — это {word}, a не "{answer}".')
            print()
    return answers

def get_result(answers):
    """принимает на вход словарь с результатами ответов и
    словарь уровня знаний, при помощи print() выводит правильно и
    неправильно отвеченные слова, и возвращает показатель уровня
    знаний согласно словаря."""
    true_anwer = 0
    false_anwer = 0
    print('Правильно отвечены слова:')
    for translation, word in answers.items():
        if word == True:
            print(f'- {translation}')
            true_anwer+=1
    if true_anwer == 0:
        print('К сожелению правильных ответов нет.')
    print('Неправильно отвечены слова:')
    for translation, word in answers.items():
        if word == False:
            print(f'- {translation}')
            false_anwer +=1
    if false_anwer == 0:
        print('Поздравляю, неправильных ответов - нет.')
    print()
    
    print(f'Варш уровень: {glossary.levels[true_anwer]}')
    return glossary.levels[true_anwer]



#Функция для сохранения информации о пройденом тесте
def current_dir(name):
    """ Путь к работающему файлу для json """
    current_dir_file = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir_file, f"{name}.json")
    return file_path

def save_result_user_name(name = 'name', difficulty_level={"family": "семья"},answers_program={"family": False},result="Нулевой"):
    """ name - имя пользователя """
    test_results = {
        "name": name,
        "level": difficulty_level,
        "answers": answers_program,
        "level_result": result
    }
    file_path = current_dir(name)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_results, file, ensure_ascii=False)

def open_result_user_name(name):
    file_path = current_dir(name)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data



