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
    
    def __init__(self,max_power=0):
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
    
    def __init__(self,socket_type='None',ram_slots=0,ssd_slots=0):
        self.socket_type = socket_type
        self.ram_slots = ram_slots
        self.ssd_slots = ssd_slots
    
    def motherboard_power_unit(self,sum_power,nums_devase):
        power_one_divase = sum_power/nums_devase
        print(f'На каждый девайс перераспределенно напряжение по {power_one_divase} Вт.')
        return math.ceil(power_one_divase)
        
#3. Центральный процессор (кол-во ядер, мощность процессора, потребляемая мощность в ваттах) + метод активировать турбо режим.

class Cpu:
    
    def __init__(self,cores=0,processor_power=0,cpu_energy_consumption=0):
        self.cores = cores
        self.processor_power = processor_power
        self.nominal_energy_consumption = cpu_energy_consumption
        self.cpu_energy_consumption = cpu_energy_consumption
    
    def on_turbo_mode_cpu(self):
        self.cpu_energy_consumption = math.ceil(self.nominal_energy_consumption*1.75) 
        print(f'Процессор работает в турбо режиме, энерго потребление вырасло с {self.nominal_energy_consumption} до {self.cpu_energy_consumption} Вт.')
        return self.cpu_energy_consumption
    
    def off_turbo_mode_cpu(self):
        self.cpu_energy_consumption = self.nominal_energy_consumption 
        print(f'Процессор работает в стандартном режиме, энерго потребление снизелось с {math.ceil(self.nominal_energy_consumption*1.75)} до {self.nominal_energy_consumption} Вт.')
        return self.cpu_energy_consumption

#4. Оперативная память (кол-во памяти на одно гнездо, частота работы памяти) + методы: загрузить данные, выгрузить данные.

class Ram:
    
    def __init__(self,amount_memory=0,frequency=0,ram_energy_consumption=0):
        self.amount_memory = amount_memory
        self.frequency = frequency
        self.ram_energy_consumption = ram_energy_consumption
        self.ram_data = []
    
    def download_ram_data(self,ram_data):
        """ Сохраняем данные на RAM накопитель в массив """
        if len(self.ram_data)<=self.amount_memory:
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
    
    def __init__(self,memory=0,ssd_energy_consumption=0):
        self.memory = memory
        self.ssd_energy_consumption = ssd_energy_consumption
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
    
    def __init__(self,video_model='', video_memory=0,vc_energy_consumption=0):
        self.video_model = video_model
        self.video_memory = video_memory
        self.vc_energy_consumption = vc_energy_consumption
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

class Сomputer:

    #def __init__(self, powerUnit, motherboard, cpu, ram, ssd, videoCard):
        #self.powerUnit = powerUnit
        #self.motherboard = motherboard
        #self.cpu = cpu
        #self.ram = ram
        #self.ssd = ssd
        #self.videoCard = videoCard
        #self.sum_energy_consumption = int(cpu.cpu_energy_consumption) + int(ram.ram_energy_consumption) + int(ssd.ssd_energy_consumption) + int(videoCard.vc_energy_consumption)
        #self.max_sum_energy_consumption = int(cpu.cpu_energy_consumption) + int(ram.ram_energy_consumption)*int(motherboard.ram_slots) + int(ssd.ssd_energy_consumption)*int(motherboard.ssd_slots) + int(videoCard.vc_energy_consumption)
    
    def __init__(self, max_power=0, socket_type='None',ram_slots=0,ssd_slots=0, cores=0,processor_power=0,cpu_energy_consumption=0, amount_memory=0,frequency=0,ram_energy_consumption=0, memory=0,ssd_energy_consumption=0, video_model='', video_memory=0,vc_energy_consumption=0):
        self.powerUnit = PowerUnit(max_power)
        self.motherboard = Motherboard(socket_type,ram_slots,ssd_slots)
        self.cpu = Cpu(cores,processor_power,cpu_energy_consumption)
        self.ram = Ram(amount_memory,frequency,ram_energy_consumption)
        self.ssd = Ssd(memory,ssd_energy_consumption)
        self.videoCard = VideoCard(video_model, video_memory,vc_energy_consumption)
        self.sum_energy_consumption = int(self.cpu.cpu_energy_consumption) + int(self.ram.ram_energy_consumption) + int(self.ssd.ssd_energy_consumption) + int(self.videoCard.vc_energy_consumption)
        self.max_sum_energy_consumption = int(self.cpu.cpu_energy_consumption) + int(self.ram.ram_energy_consumption)*int(self.motherboard.ram_slots) + int(self.ssd.ssd_energy_consumption)*int(self.motherboard.ssd_slots) + int(self.videoCard.vc_energy_consumption)
    
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
            f'      Потребление: {self.cpu.cpu_energy_consumption} Вт.\n'
            f'4. Видеокарта:\n'
            f'      Модель: {self.videoCard.video_model}\n'
            f'      Объем памяти: {self.videoCard.video_memory} Гб.\n'
            f'      Потребление: {self.videoCard.vc_energy_consumption} Вт.\n'
            f'5. Оперативная память:\n'
            f'      Объем памяти (1 шт.): {self.ram.amount_memory} Гб.\n'
            f'      Частота работы: {self.ram.frequency} МГц.\n'
            f'      Потребление(1 шт.): {self.ram.ram_energy_consumption} Вт.\n'
            f'      Объем памяти с учетом возможности материнской платы ({self.motherboard.ram_slots} шт.): {self.motherboard.ram_slots*self.ram.amount_memory} Гб.\n'
            f'      Потребление с учетом возможности материнской платы ({self.motherboard.ram_slots} шт.): {self.motherboard.ram_slots*self.ram.ram_energy_consumption} Вт.\n'
            f'6. Встроенная память SSD:\n'
            f'      Объем памяти (1 шт.): {self.ssd.memory} Гб.\n'
            f'      Потребление (1 шт.): {self.ram.ram_energy_consumption} Вт.\n'
            f'      Объем памяти с учетом возможности материнской платы ({self.motherboard.ssd_slots} шт.): {self.motherboard.ssd_slots*self.ssd.memory} Гб.\n'
            f'      Потребление с учетом возможности материнской платы ({self.motherboard.ssd_slots} шт.): {self.motherboard.ssd_slots*self.ssd.ssd_energy_consumption} Вт.\n'
            f'Сводка по энергопотреблению:\n'
            f'      Мощность от блока питания: {self.powerUnit.max_power} Вт.\n'
            f'      Минимальная потребляемая мощьность: {self.sum_energy_consumption} Вт.\n'
            f'      Максимальная потребляемая мощьность: {self.max_sum_energy_consumption} Вт.\n'
        )
    
    def motherboard_power_unit(self):
        if self.powerUnit.state_power:
            if self.powerUnit.max_power > self.max_sum_energy_consumption:    
                self.sum_energy_consumption = int(self.cpu.cpu_energy_consumption) + int(self.ram.ram_energy_consumption) + int(self.ssd.ssd_energy_consumption) + int(self.videoCard.vc_energy_consumption)
                self.max_sum_energy_consumption = int(self.cpu.cpu_energy_consumption) + int(self.ram.ram_energy_consumption)*int(self.motherboard.ram_slots) + int(self.ssd.ssd_energy_consumption)*int(self.motherboard.ssd_slots) + int(self.videoCard.vc_energy_consumption)
                self.power_one_divase = math.ceil(self.max_sum_energy_consumption/4)
                print(f'Успех! На каждый девайс перераспределенно напряжение по {self.power_one_divase} Вт.')
                return True
            elif self.powerUnit.max_power > self.sum_energy_consumption:
                self.sum_energy_consumption = int(self.cpu.cpu_energy_consumption) + int(self.ram.ram_energy_consumption) + int(self.ssd.ssd_energy_consumption) + int(self.videoCard.vc_energy_consumption)
                self.max_sum_energy_consumption = int(self.cpu.cpu_energy_consumption) + int(self.ram.ram_energy_consumption)*int(self.motherboard.ram_slots) + int(self.ssd.ssd_energy_consumption)*int(self.motherboard.ssd_slots) + int(self.videoCard.vc_energy_consumption)
                self.power_one_divase = math.ceil(self.sum_energy_consumption/4)
                print(f'Успех! Система запустилась в эконом режиме, не все девайсы работоспособны')
                print(f'    -на каждый девайс перераспределенно напряжение по {self.power_one_divase} Вт.')
                return True
            else:
                print('Провал! К сожелению системе не хватает питания, установите компоненты с меньшей энерго потреблением.')
                return False
        else:
            print(f'Для начала включите блок питания')
            return False
    
    
    def on_state_power(self):
        self.powerUnit.on_state_power()
        if self.motherboard_power_unit():
            return True
        else:
            self.powerUnit.off_state_power()
            return False
    
    def off_state_power(self):
        self.powerUnit.off_state_power()
        self.off_display_image()
    
    def on_display_image(self):
        if self.powerUnit.state_power:
            self.videoCard.on_display_image()
        else:
            print(f'Для начала включите блок питания')
    
    def off_display_image(self):
        if self.powerUnit.state_power:
            self.videoCard.off_display_image()
        else:
            print(f'Питание отсутсвует, вывод изображения уже отсутсвует')
    
    def download_ram_data(self,ram_data):
        """ Сохраняем данные на RAM накопитель в массив """
        if self.powerUnit.state_power:    
            self.ram.download_ram_data(ram_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def remove_ram_data(self,ram_data):
        """ Удаляем данные c RAM накопитель в массив """
        if self.powerUnit.state_power: 
            self.ram.remove_ram_data(ram_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def download_ssd_data(self,ssd_data):
        """ Сохраняем данные на SSD накопитель в массив """
        if self.powerUnit.state_power: 
            self.ssd.download_ssd_data(ssd_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def remove_ssd_data(self,ssd_data):
        """ Удаляем данные с SSD накопитель в массив """
        if self.powerUnit.state_power: 
            self.ssd.remove_ssd_data(ssd_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def on_turbo_mode_cpu(self):
        if self.powerUnit.state_power: 
            self.cpu.on_turbo_mode_cpu()
            if self.motherboard_power_unit():
                print(f'Потребление системы достаточно!')
                return True
            else:
                print(f'!Потребление системы не достаточно')
                return False
        else:
            print(f'Питание отсутсвует, опция недоступна')
    
    def off_turbo_mode_cpu(self):
        if self.powerUnit.state_power: 
            self.cpu.off_turbo_mode_cpu()
            self.motherboard_power_unit()
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
#computer = Сomputer(powerUnit, motherboard, cpu, ram, ssd, videoCard)

computer = Сomputer(650,'AM4', 4, 1,8,3.6,65,8,3600,5,1000, 5,'GeForce RTX 4060 Ti', 8, 500)

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
