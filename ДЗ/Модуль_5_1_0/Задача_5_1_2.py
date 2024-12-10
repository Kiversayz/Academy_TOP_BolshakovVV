""" У вас есть кортеж из следующих жанров кино:
cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
Вам необходимо:
заменить жанр Экшн на Боевик
добавить жанр по вашему выбору между жанрами боевик, и
пеплум (я выбрал Фэнтези) вы можете выбрать что хотите.
Результат вывести в консоль
преобразовать полученный кортеж в строку. Результат вывести в
консоль
Вы можете преобразовывать кортежи в другой тип данных или
записывать их в новые переменные. Результат работы программы
должен выглядеть следующим образом:
(2й пункт)
('Комедия','Боевик','Фэнтези','Пеплум','Триллер')
(3й пункт)
Обновленные жанры кино: Комедия, Боевик, Фэнтези, Пеплум,Триллер
 """

cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
print(f'Исходный кортеж: {cinema_genres}')
print()
#заменить жанр Экшн на Боевик

list_cinema_genres = list(cinema_genres)
list_cinema_genres[1] = 'Боевик'
new_cinema_genres = tuple(list_cinema_genres)
print(f'Заменить жанр Экшн на Боевик через списки:{new_cinema_genres}')

index_from_element = cinema_genres.index('Экшн')
new_cinema_genres_gluing = cinema_genres[:index_from_element] + ('Боевик',) + cinema_genres[index_from_element+1:]
print(f'Заменить жанр Экшн на Боевик через срезы:{new_cinema_genres_gluing}')

#добавить жанр по вашему выбору между жанрами боевик
new_cinema_genres_gluing = cinema_genres[:index_from_element+1] + ('Ужасы',) + cinema_genres[index_from_element+1:]
print(f'Добавить жанр "Ужасы" после Экшн через срезы:{new_cinema_genres_gluing}')

#преобразовать полученный кортеж в строку.
str_new_cinema_genres_gluing = ", ".join(new_cinema_genres_gluing)
print(f'Вывод в виде строки: {str_new_cinema_genres_gluing}')

#Вы можете преобразовывать кортежи в другой тип данных или записывать их в новые переменные.
list_cinema_genres = list(cinema_genres)
print(f'Вывод в виде списка: {list_cinema_genres}')