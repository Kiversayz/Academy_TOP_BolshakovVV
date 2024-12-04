""" Напишите функцию, которая проверяет является ли
число простым. Число передаётся в качестве параметра.
Если число простое нужно вернуть из метода true, иначе
false. """

#is_prime

def простое_число (num):
    if num == 1 or num == 0:
        return False
    else:
        for a in range (2, num):
            if num%a == 0:
                return False
        else:
            return True
