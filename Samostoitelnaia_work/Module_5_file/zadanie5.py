""" Задание 5
Дан текстовый файл. Подсчитать количество слов,
начинающихся с символа, который задаёт пользователь. """


poisk_vvod = input("Введите букву и мы будим считать все слова на неё: ")

stetchik = 0

with open("Praktika_work/Module_5_file/kakoitotext.txt", 'r',encoding="utf-8") as file:
    spisok_slova = file.read().split()
    #print(lines)
    #print(lines.split())
    
    for slovo in spisok_slova:
        if slovo[0].lower() == poisk_vvod.lower():
            stetchik +=1

print(stetchik)