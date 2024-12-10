""" Напишите функцию, которая возвращает минимальное из
пяти чисел. Числа передаются в качестве параметров. """

def min_arg (*arg):
    min_znach = arg[0]
    print(min_znach)
    for i in arg:
            print(i)
            if min_znach > i:
                min_znach = i
            else:
                continue
    return min_znach


print(f'{min_arg(3,4,56,6)} = итог 4')
