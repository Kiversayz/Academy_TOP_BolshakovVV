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
#1. Блок питания (мощность в ваттах).

class PowerUnit:
    
    def __init__(self,max_power):
        self.max_power = max_power

#2. Материнская плата (тип гнезда процессора, кол-во гнезд оперативной памяти, кол-во гнезд для SSD).
class Motherboard:
    
    def __init__(self,socket_type,ram_slots,ssd_slots):
        self.socket_type = socket_type
        self.ram_slots = ram_slots
        self.ssd_slots = ssd_slots

#3. Центральный процессор (кол-во ядер, мощность процессора, потребляемая мощность в ваттах).

class Cpu:
    
    def __init__(self,cores,processor_power,energy_consumption):
        self.cores = cores
        self.processor_power = processor_power
        self.energy_consumption = energy_consumption

#4. Оперативная память (кол-во памяти на одно гнездо, частота работы памяти) + методы: загрузить данные, выгрузить данные.

class Ram:
    
    def __init__(self,amount_memory,frequency,energy_consumption):
        self.amount_memory = amount_memory
        self.frequency = frequency
        self.energy_consumption = energy_consumption
        self.ram_data = []
    
    def download_data(self,ram_data):
        """ Сохраняем данные на RAM накопитель в массив """
        self.ram_data.append(ram_data)
        print(f'{ram_data} было загруженно на SSD накопитель.')
        return self.ram_data
    
    def remove_data(self,ram_data):
        """ Удаляем данные c RAM накопитель в массив """
        if ram_data in self.ram_data:
            self.ram_data.remove(ram_data)
            print(f'{ram_data} было удалено с SSD накопитель.')
            return self.ram_data
        print(f'{ram_data} не найден на SSD накопителе')
        return self.ram_data

#5. SSD-накопитель (объем памяти) + методы: загрузить данные, выгрузить данные.

class Ssd:
    
    def __init__(self,memory,energy_consumption):
        self.memory = memory
        self.energy_consumption = energy_consumption
        self.ssd_data = []
    
    def download_data(self,ssd_data):
        """ Сохраняем данные на SSD накопитель в массив """
        self.ssd_data.append(ssd_data)
        print(f'{ssd_data} было загруженно на SSD накопитель.')
        return self.ssd_data
    
    def remove_data(self,ssd_data):
        """ Удаляем данные с SSD накопитель в массив """
        if ssd_data in self.ssd_data:
            self.ssd_data.remove(ssd_data)
            print(f'{ssd_data} было удалено с SSD накопитель.')
            return ssd_data
        print(f'{ssd_data} не найден на SSD накопителе')
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
        


powerUnit = PowerUnit(700)
motherboard = Motherboard('AM4', 4, 1)
cpu = Cpu(8,3.6,65)
ram = Ram(8,3600,5)
ssd = Ssd(1000, 5)
videoCard = VideoCard('GeForce RTX 4060 Ti', 8, 500)

computer = Сomputer(powerUnit, motherboard, cpu, ram, ssd, videoCard)

print('Получаем информацию о сборке!')
print(computer.computer_specifications())
print()

print('Вкл/Выкл трансляции изображения')
computer.videoCard.off_display_image()
computer.videoCard.on_display_image()
print()

print('Сохранение и удаление на SSD')
computer.ssd.download_data('Привет, Мир!')
computer.ssd.download_data('Как дела, Мир?')
computer.ssd.remove_data('Привет, Мир!')
print()

print('Сохранение и удаление на RAM')
computer.ram.download_data('Привет, оперативка!')
computer.ram.download_data('Как дела, оперативка?')
computer.ram.remove_data('Привет, оперативка!')