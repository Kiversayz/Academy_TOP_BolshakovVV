""" Модуль 4/1 - 2
Напишите функцию, которая принимает два числа в качестве
параметра и отображает все четные числа между ними """

def even_numbers_str (arg1, arg2):
    if arg1>arg2: #хочу видеть аргумент arg1<arg2
        arg1,arg2 = arg2,arg1 #меняю числа между собой, для обеспечения работоспособности
    evenNumbers = ""
    for number in range(arg1, arg2+1):
        if number%2==0:
            evenNumbers=evenNumbers+str(number)+" "
        else:
            continue
    return evenNumbers

print(f'Введите два аргумента:')
print(f'Четные числа в данном диапозоне: {even_numbers_str(int(input()),int(input()))}')