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
import json
import os

# Относительный путь к JSON-файлу
DATA_PATH = os.path.join("DZ", "Module_5_1_2", "data.json")
RESULTS_DIR = os.path.join("DZ", "Module_5_1_2", "result")

def load_data(file_name=DATA_PATH):
    """Загружает слова и уровни из JSON-файла"""
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)

def get_user_level(level_input, data):
    """Определяет уровень сложности, если нет совпадений — ставит легкий"""
    level_map = {
        "легкий": "easy",
        "средний": "medium",
        "тяжелый": "hard"
    }
    return data["questions"].get(level_map.get(level_input.lower().strip(), "easy"))

def ask_questions(words):
    """Задает вопросы пользователю и собирает ответы"""
    answers = {}
    for word, translation in words.items():
        print(f'{word}, {len(translation)} букв, начинается на {translation[0]}...')
        user_answer = input("Введите перевод: ").strip().lower()
        answers[word] = user_answer == translation.lower()
        print(f"{'Верно' if answers[word] else f'Неверно, {word} — это {translation}'}\n")
    return answers

def evaluate_results(answers, data):
    """Определяет уровень пользователя по количеству правильных ответов"""
    correct_answers = sum(answers.values())
    print("\nПравильные ответы:", [w for w, r in answers.items() if r] or "Нет правильных ответов")
    print("Неправильные ответы:", [w for w, r in answers.items() if not r] or "Все правильно!")
    print("\nВаш уровень:", data["levels"][str(correct_answers)])
    return data["levels"][str(correct_answers)]

def save_results(name, level, answers, result):
    """Сохраняет результаты теста в JSON"""
    file_path = os.path.join(RESULTS_DIR, f"{name}.json")
    test_results = {
        "name": name,
        "level": level,
        "answers": answers,
        "level_result": result
    }
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_results, file, ensure_ascii=False, indent=4)
    print(f"Результаты сохранены в {file_path}")



