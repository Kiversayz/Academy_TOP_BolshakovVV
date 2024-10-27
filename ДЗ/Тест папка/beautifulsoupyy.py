from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>Тестовая страница</title></head>
<body>
    <h1>Привет, мир!</h1>
    <p>Это тестовый параграф.</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Проверка заголовка
assert soup.title.string == "Тестовая страница", "Заголовок не совпадает!"

# Проверка h1
assert soup.h1.string == "Привет, мир!", "Заголовок h1 не совпадает!"

print("Все тесты пройдены успешно!")

print(dir(BeautifulSoup))