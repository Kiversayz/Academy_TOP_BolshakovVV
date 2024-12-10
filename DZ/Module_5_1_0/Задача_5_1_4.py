""" У вас есть список:
cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия",
"пеплум"]
Вам необходимо:
преобразовать данный список в множество;
добавить 2 жанра на ваш выбор (то что вы захотите);
удалить какой-то из жанров по вашему выбору;
удалить некий случайный жанр;
преобразовать множество обратно в список. """

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия","пеплум"]
print(f'Список: {cinema_genres}')

#преобразовать данный список в множество;

cinema_genres = set(cinema_genres)
print(f'Множество: {cinema_genres}')

#добавить 2 жанра на ваш выбор (то что вы захотите);
add_one = input('Добавим жанр: ')
cinema_genres.add(add_one)
add_two = input('Еще один жанр: ')
cinema_genres.add(add_two)

print(f'Обновленная новыми жанрами "{add_one}" и "{add_two}": {cinema_genres}')

#удалить какой-то из жанров по вашему выбору;
print('Удалим жанр "комедия"')
cinema_genres.remove("комедия")
print(f'Обновленная c удаленным жанром "комедия": {cinema_genres}')
print('Удалим жанр "пеплум"')
cinema_genres.discard("пеплум")
print(f'Обновленная c удаленным жанром "пеплум": {cinema_genres}')
print('Удалим случайный жанр')
random_genres = list(cinema_genres)
print(random_genres[0])
cinema_genres-={random_genres[0]}
print(f'Обновленная c удаленным жанром "{random_genres[0]}": {cinema_genres}')

#преобразовать множество обратно в список.
cinema_genres = list(cinema_genres)
print(f'Преобразовали обратно в список {cinema_genres}')
