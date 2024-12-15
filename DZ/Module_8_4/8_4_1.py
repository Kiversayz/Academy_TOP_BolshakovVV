import math
""" 
Ваша задача в этом задании собрать персональный компьютер
из компонентов которые в него входят:

1. блок питания - атрибут мощность/метод подать
напряжение;
2. материнская плата - атрибут чипсет/метод
перераспределить напряжение от БП по компонентам;
3. центральный процессор - атрибуты: тактовая частота,
количество ядер/метод активировать турбо режим
4. оперативная память - атрибуты: объем памяти, частота
памяти/методы: загрузить данные, выгрузить данные
5. SSD накопитель - атрибуты: объем/методы сохранить
данные, удалить данные.
6. видеокарта - атрибуты: модель видеокарты, объем памяти/
метод: вывести изображение на экран

Реализовать данный компьютер при помощи и
множественного наследования и композиции
(по факту тут 2 задачи в одной).
"""

""" 
-У каждого класса есть потребляемая мощность, кроме «материнская плата» и «блок питания».

-Есть класс, который дает предел мощности, — «блок питания». 

1. Блок питания (мощность в ваттах).

2. Материнская плата (тип гнезда процессора, кол-во гнезд оперативной памяти, кол-во гнезд для SSD).

3. Центральный процессор (кол-во ядер, мощность процессора, потребляемая мощность в ваттах).

4. Оперативная память (кол-во памяти на одно гнездо, частота работы памяти) + методы: загрузить данные, выгрузить данные.

5. SSD-накопитель (объем памяти) + методы: загрузить данные, выгрузить данные.

6. Видеокарта (модель, объем памяти) + метод: вывести изображение на экран.
"""
#1. Блок питания (мощность в ваттах) + метод подать напряжение.

class PowerUnit:
    
    def __init__(self,max_power):
        self.max_power = max_power
        self.state_power = False
    
    def on_state_power(self):
        if self.state_power == False:
            self.state_power = True
            print(f'Питание влючено')
            return self.state_power
        print('Питание уже включено')
        return self.state_power
    
    def off_state_power(self):
        if self.state_power == True:
            self.state_power = False
            print(f'Питание выключено')
            return self.state_power
        print('Питание уже выключено')
        return self.state_power

#2. Материнская плата (тип гнезда процессора, кол-во гнезд оперативной памяти, кол-во гнезд для SSD) + метод
# перераспределить напряжение от БП по компонентам.
class Motherboard:
    
    def __init__(self,socket_type,ram_slots,ssd_slots):
        self.socket_type = socket_type
        self.ram_slots = ram_slots
        self.ssd_slots = ssd_slots
    
    def motherboard_power_unit(self,sum_power,nums_devase):
        power_one_divase = sum_power/nums_devase
        print(f'На каждый девайс перераспределенно напряжение по {power_one_divase} Вт.')
        return math.ceil(power_one_divase)
        
#3. Центральный процессор (кол-во ядер, мощность процессора, потребляемая мощность в ваттах) + метод активировать турбо режим.

class Cpu:
    
    def __init__(self,cores,processor_power,energy_consumption):
        self.cores = cores
        self.processor_power = processor_power
        self.nominal_energy_consumption = energy_consumption
        self.energy_consumption = energy_consumption
    
    def on_turbo_mode_cpu(self):
        naminal = self.energy_consumption
        self.energy_consumption = math.ceil(self.nominal_energy_consumption*1.75) 
        print(f'Процессор работает в турбо режиме, энерго потребление вырасло с {naminal} до {self.energy_consumption} Вт.')
        return self.energy_consumption
    
    def off_turbo_mode_cpu(self):
        naminal = self.energy_consumption
        self.energy_consumption = self.nominal_energy_consumption 
        print(f'Процессор работает в стандартном режиме, энерго потребление снизелось с {naminal} до {self.energy_consumption} Вт.')
        return self.energy_consumption

#4. Оперативная память (кол-во памяти на одно гнездо, частота работы памяти) + методы: загрузить данные, выгрузить данные.

class Ram:
    
    def __init__(self,amount_memory,frequency,energy_consumption):
        self.amount_memory = amount_memory
        self.frequency = frequency
        self.energy_consumption = energy_consumption
        self.ram_data = []
    
    def download_ram_data(self,ram_data):
        """ Сохраняем данные на RAM накопитель в массив """
        if len(ram_data)<=self.amount_memory:
            self.ram_data.append(ram_data)
            print(f'"{ram_data}" было загруженно на RAM накопитель.')
            return self.ram_data
        else:
            print(f'Память RAM перегружена, запись "{ram_data}" не возможна')
            return self.ram_data
    
    def remove_ram_data(self,ram_data):
        """ Удаляем данные c RAM накопитель в массив """
        if ram_data in self.ram_data:
            self.ram_data.remove(ram_data)
            print(f'"{ram_data}" было удалено  RAM накопитель.')
            return self.ram_data
        print(f'"{ram_data}" не найден на  RAM накопителе')
        return self.ram_data

#5. SSD-накопитель (объем памяти) + методы: загрузить данные, выгрузить данные.

class Ssd:
    
    def __init__(self,memory,energy_consumption):
        self.memory = memory
        self.energy_consumption = energy_consumption
        self.ssd_data = []
    
    def download_ssd_data(self,ssd_data):
        """ Сохраняем данные на SSD накопитель в массив """
        self.ssd_data.append(ssd_data)
        print(f'"{ssd_data}" было загруженно на SSD накопитель.')
        return self.ssd_data
    
    def remove_ssd_data(self,ssd_data):
        """ Удаляем данные с SSD накопитель в массив """
        if ssd_data in self.ssd_data:
            self.ssd_data.remove(ssd_data)
            print(f'"{ssd_data}" было удалено с SSD накопитель.')
            return ssd_data
        print(f'"{ssd_data}" не найден на SSD накопителе')
        return self.ssd_data


#6. Видеокарта (модель, объем памяти) + метод: вывести изображение на экран.

class VideoCard:
    
    def __init__(self,video_model, video_memory,energy_consumption):
        self.video_model = video_model
        self.video_memory = video_memory
        self.energy_consumption = energy_consumption
        self.display_image = False
    
    def on_display_image(self):
        if self.display_image == False:
            self.display_image = True
            print(f'Включен режим вывода изображения на экран')
            return self.display_image
        print('Режим вывода изображения на экран уже включен')
        return self.display_image
    
    def off_display_image(self):
        if self.display_image == True:
            self.display_image = False
            print(f'Выключен режим вывода изображения на экран')
            return self.display_image
        print('Режим вывода изображения на экран уже выключен')
        return self.display_image

#Реализовать данный компьютер при помощи и
# множественного наследования и композиции

class Сomputer():

    def __init__(self, powerUnit, motherboard, cpu, ram, ssd, videoCard):
        self.powerUnit = powerUnit
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.videoCard = videoCard
        self.sum_energy_consumption = int(cpu.energy_consumption) + int(ram.energy_consumption) + int(ssd.energy_consumption) + int(videoCard.energy_consumption)
        self.max_sum_energy_consumption = int(cpu.energy_consumption) + int(ram.energy_consumption)*int(motherboard.ram_slots) + int(ssd.energy_consumption)*int(motherboard.ssd_slots) + int(videoCard.energy_consumption)
    
    def computer_specifications(self):
        return (
            f'Сборка компьютера состоит из:\n'
            f'1. Материнская плата:\n'
            f'      Тип чипсета: {self.motherboard.socket_type}\n'
            f'      Кол-во слотов для RAM памяти: {self.motherboard.ram_slots} шт.\n'
            f'      Кол-во слотов для SSD памяти: {self.motherboard.ssd_slots} шт.\n'
            f'2. Блок питания:\n'
            f'      Мощность: {self.powerUnit.max_power} Вт.\n'
            f'3. Процессор:\n'
            f'      Кол-во ядер: {self.cpu.cores} шт.\n'
            f'      Кол-во потоков: {self.cpu.cores*2} шт.\n'
            f'      Частота работы ядра: {self.cpu.processor_power} ГГц.\n'
            f'      Потребление: {self.cpu.energy_consumption} Вт.\n'
            f'4. Видеокарта:\n'
            f'      Модель: {self.videoCard.video_model}\n'
            f'      Объем памяти: {self.videoCard.video_memory} Гб.\n'
            f'      Потребление: {self.videoCard.energy_consumption} Вт.\n'
            f'5. Оперативная память:\n'
            f'      Объем памяти (1 шт.): {self.ram.amount_memory} Гб.\n'
            f'      Частота работы: {self.ram.frequency} МГц.\n'
            f'      Потребление(1 шт.): {self.ram.energy_consumption} Вт.\n'
            f'      Объем памяти с учетом возможности материнской платы ({self.motherboard.ram_slots} шт.): {self.motherboard.ram_slots*self.ram.amount_memory} Гб.\n'
            f'      Потребление с учетом возможности материнской платы ({self.motherboard.ram_slots} шт.): {self.motherboard.ram_slots*self.ram.energy_consumption} Вт.\n'
            f'6. Встроенная память SSD:\n'
            f'      Объем памяти (1 шт.): {self.ssd.memory} Гб.\n'
            f'      Потребление (1 шт.): {self.ram.energy_consumption} Вт.\n'
            f'      Объем памяти с учетом возможности материнской платы ({self.motherboard.ssd_slots} шт.): {self.motherboard.ssd_slots*self.ssd.memory} Гб.\n'
            f'      Потребление с учетом возможности материнской платы ({self.motherboard.ssd_slots} шт.): {self.motherboard.ssd_slots*self.ssd.energy_consumption} Вт.\n'
            f'Сводка по энергопотреблению:\n'
            f'      Мощность от блока питания: {self.powerUnit.max_power} Вт.\n'
            f'      Минимальная потребляемая мощьность: {self.sum_energy_consumption} Вт.\n'
            f'      Максимальная потребляемая мощьность: {self.max_sum_energy_consumption} Вт.\n'
        )
    
    def motherboard_power_unit(self):
        if powerUnit.state_power:
            if powerUnit.max_power > self.max_sum_energy_consumption:    
                power_one_divase = math.ceil(self.max_sum_energy_consumption/4)
                print(f'Успех! На каждый девайс перераспределенно напряжение по {power_one_divase} Вт.')
                return True
            elif powerUnit.max_power > sum_energy_consumption:
                power_one_divase = math.ceil(self.max_sum_energy_consumption/4)
                print(f'Успех! Система запустилась в эконом режиме, не все девайсы работоспособны')
                print(f'    -на каждый девайс перераспределенно напряжение по {power_one_divase} Вт.')
                return True
            else:
                print('Провал! К сожелению системе не хватает питания, установите компоненты с меньшей энерго потреблением.')
                return False
        else:
            print(f'Для начала включите блок питания')
            return False
    
    
    def on_state_power(self):
        powerUnit.on_state_power()
    
    def off_state_power(self):
        powerUnit.off_state_power()
        self.off_display_image()
    
    def on_display_image(self):
        if powerUnit.state_power:
            videoCard.on_display_image()
        else:
            print(f'Для начала включите блок питания')
    
    def off_display_image(self):
        if powerUnit.state_power:
            videoCard.off_display_image()
        else:
            print(f'Питание отсутсвует, вывод изображения уже отсутсвует')
    
    def download_ram_data(self,ram_data):
        """ Сохраняем данные на RAM накопитель в массив """
        if powerUnit.state_power:    
            self.ram.download_ram_data(ram_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def remove_ram_data(self,ram_data):
        """ Удаляем данные c RAM накопитель в массив """
        if powerUnit.state_power: 
            self.ram.remove_ram_data(ram_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def download_ssd_data(self,ssd_data):
        """ Сохраняем данные на SSD накопитель в массив """
        if powerUnit.state_power: 
            self.ssd.download_ssd_data(ssd_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def remove_ssd_data(self,ssd_data):
        """ Удаляем данные с SSD накопитель в массив """
        if powerUnit.state_power: 
            self.ssd.remove_ssd_data(ssd_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def on_turbo_mode_cpu(self):
        if powerUnit.state_power: 
            cpu.on_turbo_mode_cpu()
            if self.motherboard_power_unit():
                print('Турбо режим успешно запущен')
            else:
                self.off_turbo_mode_cpu(self)
        else:
            print(f'Питание отсутсвует, опция недоступна')
    
    def off_turbo_mode_cpu(self):
        if powerUnit.state_power: 
            cpu.off_turbo_mode_cpu()
        else:
            print(f'Питание отсутсвует, опция недоступна')


powerUnit = PowerUnit(700)
motherboard = Motherboard('AM4', 4, 1)
cpu = Cpu(8,3.6,65)
ram = Ram(8,3600,5)
ssd = Ssd(1000, 5)
videoCard = VideoCard('GeForce RTX 4060 Ti', 8, 500)

print('Вкл/Выкл трансляции изображения')
videoCard.off_display_image()
videoCard.on_display_image()
videoCard.off_display_image()
print()

print('Сохранение и удаление на SSD')
ssd.download_ssd_data('Привет, Мир!')
ssd.download_ssd_data('Как дела, Мир?')
ssd.remove_ssd_data('Привет, Мир!')
ssd.remove_ssd_data('Как дела, Мир?')
ssd.remove_ssd_data('Nan')
print()

print('Сохранение и удаление на RAM')
ram.download_ram_data('Привет, оперативка!')
ram.download_ram_data('Как дела, оперативка?')
ram.remove_ram_data('Привет, оперативка!')
ram.remove_ram_data('Как дела, оперативка?')
ram.remove_ram_data('Nan')
print()

powerUnit.on_state_power()
powerUnit.off_state_power()
print()

motherboard.motherboard_power_unit(800,5)
print()

cpu.on_turbo_mode_cpu()
cpu.off_turbo_mode_cpu()

print()
computer = Сomputer(powerUnit, motherboard, cpu, ram, ssd, videoCard)

print('Получаем информацию о сборке!')
print(computer.computer_specifications())
print()

print('Вкл/Выкл трансляции изображения в ПК')
computer.on_state_power()
computer.on_display_image()
computer.off_display_image()
computer.off_state_power()
computer.on_state_power()
computer.download_ram_data('Привет, оперативка!')
computer.motherboard_power_unit()
computer.remove_ram_data('Привет, оперативка!')
computer.remove_ram_data('Привет!')
computer.download_ssd_data('Тук-Тук')
computer.remove_ssd_data('Привет!')
computer.remove_ssd_data('Тук-Тук')
computer.on_turbo_mode_cpu()
computer.off_turbo_mode_cpu()
