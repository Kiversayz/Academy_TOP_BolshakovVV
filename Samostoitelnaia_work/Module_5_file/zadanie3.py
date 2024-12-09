""" Задание 3
Дан текстовый файл. Необходимо переписать его
строки в другой файл. Порядок строк во втором файле
должен быть обратным по отношению к порядку строк
в заданном файле. """

with open("Praktika_work/Module_5_file/kakoitotext.txt", 'r',encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
    with open("Praktika_work/Module_5_file/kakoitotext_revers.txt", 'w',encoding="utf-8") as file_revers:
        file_revers.writelines(lines[::-1])
        print(f"Файл записан kakoitotext_revers.txt")