""" Напишите функцию, которая возвращает минимальное из
пяти чисел. Числа передаются в качестве параметров. """

def min_arg (arg1=0,arg2=0,arg3=0,arg4=0,arg5=0):
    min_znach = arg1
    for i in (arg2,arg3,arg4,arg5):
        if min_znach > i:
            min_znach = i
        else:
            continue
    return min_znach

print(min_arg(13,7,5,4,22))
