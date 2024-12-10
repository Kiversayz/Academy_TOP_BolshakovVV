
""" 
Задача 1
У вас есть абстракция учитель, вам надо написать класс
согласно этой абстракции характеристики класса:
Поля (атрибуты) класса class Teacher:
имя (name) в примере Иван Петров;
образование (education) в примере БГПУ;
опыт работы (experience) в примере 4 года;
Все атрибуты необходимо сделать защищенными.
Для данных атрибутов необходимо написать геттеры (для всех)
а для атрибута опыт работы (experience) также необходим еще и
сеттер.
Методы класса Teacher.
get_teacher_data возвращает информацию об учителе
результат вызова метода:
add_mark в качестве аргументов принимает имя студента и
его оценку, результат вызова метода:
remove_mark в качестве аргументов принимает имя
студента и его оценку, результат вызова метода:
give_a_consultation в качестве аргумента принимает, класс
в котором учатся ученики, результат вызова метода:
"""

class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience
        return self.__experience

    def get_teacher_data(self):
        return f"{self.get_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} лет."

    def add_mark(self, student_name, mark):
        # student_name - ФИО студента, mark - оценка которую поставил препод
        return f"{self.get_name()} поставил оценку {mark} студенту {student_name}."

    def remove_mark(self, student_name, mark):
        # student_name - ФИО студента, mark - оценка которую удалил препод
        return f"{self.get_name()} удалил оценку {mark} студенту {student_name}."

    def give_a_consultation(self, student_class):
        # Пример реализации
        return f"{self.get_name()} Провел консультацию в классе {student_class}."

print('Задание №1')
teacherTeacher = Teacher('Большаков Валерий', 'БГПУ','5')

print(teacherTeacher.get_education(),teacherTeacher.get_experience(),teacherTeacher.get_name())

print(teacherTeacher.get_teacher_data())
print('Изменим возраст с 5 на 6 лет стажа')

teacherTeacher.set_experience('6')

print(teacherTeacher.get_teacher_data())
print()

print(teacherTeacher.add_mark('Антонов Антон', 5))
print(teacherTeacher.remove_mark('Попов Антон', 3))
print(teacherTeacher.give_a_consultation('7-ое МВД'))

print()
print()
print('Задание №2')
""" 
Задача 2
Написать класс наследник DisciplineTeacher, его классом
родителем (базовым классом) будет класс Teacher, ему
необходимо добавить 2 новых атрибута.
discipline - предмет его надо перенести из класса Teacher;
job_title - должность (например завуч, директор, учитель
старших классов).
Все атрибуты необходимо сделать защищенными.
Для данных атрибутов необходимо написать геттеры (для всех)
а для атрибута job_title также необходим еще и сеттер.
Далее необходимо адаптировать методы класса родителя а
именно:
get_teacher_data
add_mark
remove_mark
give_a_consultation
Ниже приведены примеры вызова методов
"""

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, value):
        self.__job_title = value
        return self.__job_title

    def get_teacher_data(self):
        return f"{self.get_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} лет.\nПредмет {self.get_discipline()}, должность {self.get_job_title()}"

    def add_mark(self, student_name, mark):
        # Адаптация метода add_mark
        return f"{self.get_name()} поставил оценку {mark} студенту {student_name}.\nПредмет {self.get_discipline()}"

    def remove_mark(self, student_name, mark):
        # Адаптация метода remove_mark
        return f"{self.get_name()} удалил оценку {mark} студенту {student_name}.\nПредмет {self.get_discipline()}"

    def give_a_consultation(self, student_class):
        # Адаптация метода give_a_consultation
        return f"{self.get_name()} Провел консультацию в классе {student_class}.\nПо предмету {self.get_discipline()} как {self.get_job_title()}"

DisciplineTeacher = DisciplineTeacher('Стариков Ванадий', 'БГПУ','70','Программирование', 'Студент')

print(DisciplineTeacher.get_education(),DisciplineTeacher.get_experience(),DisciplineTeacher.get_name(),DisciplineTeacher.get_job_title(),DisciplineTeacher.get_discipline())

print(DisciplineTeacher.get_teacher_data())
print('Изменим возраст с 70 на 5 лет стажа')

DisciplineTeacher.set_experience('5')

print(DisciplineTeacher.get_teacher_data())
print()

print(DisciplineTeacher.add_mark('Антонов Антон', 5))
print(DisciplineTeacher.remove_mark('Попов Антон', 3))
print(DisciplineTeacher.give_a_consultation('8Б'))