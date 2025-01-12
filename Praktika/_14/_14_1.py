""" 
Задание 1
Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в односвязный
список. После чего нужно показать меню, в котором
предложить пользователю набор пунктов:
1. Добавить элемент в список.
2. Удалить элемент из списка.
3. Показать содержимое списка.
4. Проверить есть ли значение в списке.
5. Заменить значение в списке.
В зависимости от выбора пользователя выполняется
действие, после чего меню отображается снова.
"""

class Node:
    
    def __init__ (self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    
    def __init__ (self):
        self.head = None
        self.end = None
    
    def clear_node (self,data):
        if not self.head:
            return None
        if self.head.data == data:
            self.head.data = data
            return f'new_data = {self.head.data}'
        current_node = self.head
        while current_node and current_node.next_node:
            if current_node