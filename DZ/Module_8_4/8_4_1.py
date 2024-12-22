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

class Device:
    """Базовый класс для устройств."""
    def __init__(self, energy_consumption=0):
        self.energy_consumption = energy_consumption

class StorageDevice(Device):
    """Базовый класс для устройств хранения данных с учетом ограничения памяти."""
    def __init__(self, memory=0, energy_consumption=0):
        super().__init__(energy_consumption)
        self.memory = memory  # Максимальный объем памяти
        self.data = []        # Хранилище данных

    def download_data(self, data):
        """Сохраняет данные в устройство, если хватает места."""
        if len(self.data) < self.memory:
            self.data.append(data)
            print(f"Данные '{data}' загружены в хранилище.")
        else:
            print(f"Хранилище заполнено. Данные '{data}' не могут быть записаны.")

    def remove_data(self, data):
        """Удаляет данные из устройства."""
        if data in self.data:
            self.data.remove(data)
            print(f"Данные '{data}' удалены из хранилища.")
        else:
            print(f"Данные '{data}' не найдены в хранилище.")

    def get_available_space(self):
        """Возвращает количество оставшихся свободных мест в хранилище."""
        return self.memory - len(self.data)


#1. Блок питания (мощность в ваттах) + метод подать напряжение.

class PowerUnit:
    """ Блок питания. """
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
    
    def distribute_power(self,sum_power,nums_devase):
        power_one_divase = sum_power/nums_devase
        print(f'На каждый девайс перераспределенно напряжение по {power_one_divase} Вт.')
        return math.ceil(power_one_divase)
        
#3. Центральный процессор (кол-во ядер, мощность процессора, потребляемая мощность в ваттах) + метод активировать турбо режим.

class Cpu(Device):
    
    def __init__(self,cores=0,processor_power=0,energy_consumption=0):
        super().__init__(energy_consumption)
        self.cores = cores
        self.processor_power = processor_power
        self.nominal_energy_consumption = energy_consumption
    
    def on_turbo_mode_cpu(self):
        self.energy_consumption = math.ceil(self.nominal_energy_consumption*1.75) 
        print(f'Процессор работает в турбо режиме, энерго потребление вырасло с {self.nominal_energy_consumption} до {self.energy_consumption} Вт.')
        return self.energy_consumption
    
    def off_turbo_mode_cpu(self):
        self.energy_consumption = self.nominal_energy_consumption 
        print(f'Процессор работает в стандартном режиме, энерго потребление снизелось с {math.ceil(self.nominal_energy_consumption*1.75)} до {self.nominal_energy_consumption} Вт.')
        return self.energy_consumption

#4. Оперативная память (кол-во памяти на одно гнездо, частота работы памяти) + методы: загрузить данные, выгрузить данные.

class Ram(StorageDevice):
    """Класс для оперативной памяти."""
    def __init__(self, memory=0, frequency=0, energy_consumption=0):
        super().__init__(memory, energy_consumption)
        self.frequency = frequency
    
    def download_data(self, data):
        """Сохраняет данные в RAM."""
        if len(self.data) < self.memory:
            self.data.append(data)
            print(f"Данные '{data}' загружены в RAM.")
        else:
            print(f"RAM заполнен. Данные '{data}' не могут быть записаны.")
    
    def remove_data(self, data):
        """Удаляет данные из RAM."""
        if data in self.data:
            self.data.remove(data)
            print(f"Данные '{data}' удалены из RAM.")
        else:
            print(f"Данные '{data}' не найдены в RAM.")
    
    def get_specifications(self):
        return (
            f"Оперативная память:\n"
            f"  Объем: {self.memory} ГБ\n"
            f"  Частота: {self.frequency} МГц\n"
            f"  Энергопотребление: {self.energy_consumption} Вт\n"
        )

#5. SSD-накопитель (объем памяти) + методы: загрузить данные, выгрузить данные.

class Ssd(StorageDevice):
    """Класс для SSD-накопителя."""
    def __init__(self, memory=0, energy_consumption=0):
        super().__init__(memory, energy_consumption)
    
    def download_data(self, data):
        """Сохраняет данные в SSD."""
        if len(self.data) < self.memory:
            self.data.append(data)
            print(f"Данные '{data}' загружены в SSD.")
        else:
            print(f"SSD заполнен. Данные '{data}' не могут быть записаны.")
    
    def remove_data(self, data):
        """Удаляет данные из SSD."""
        if data in self.data:
            self.data.remove(data)
            print(f"Данные '{data}' удалены из SSD.")
        else:
            print(f"Данные '{data}' не найдены в SSD.")
    
    def get_specifications(self):
        return (
            f"SSD-накопитель:\n"
            f"  Объем: {self.memory} ГБ\n"
            f"  Энергопотребление: {self.energy_consumption} Вт\n"
        )

#6. Видеокарта (модель, объем памяти) + метод: вывести изображение на экран.

class VideoCard(Device):
    
    def __init__(self,video_model='', video_memory=0,energy_consumption=0):
        super().__init__(energy_consumption)
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

class Сomputer:


    def __init__(self, power_unit, motherboard, cpu, ram, ssd, video_card):
        self.power_unit = power_unit
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.video_card = video_card
        self.update_energy_consumption()

    def update_energy_consumption(self):
        """Обновляет минимальное и максимальное энергопотребление системы."""
        self.sum_energy_consumption = (
            self.cpu.energy_consumption +
            self.ram.energy_consumption +
            self.ssd.energy_consumption +
            self.video_card.energy_consumption
        )
        self.max_sum_energy_consumption = (
            self.cpu.energy_consumption +
            self.ram.energy_consumption * self.motherboard.ram_slots +
            self.ssd.energy_consumption * self.motherboard.ssd_slots +
            self.video_card.energy_consumption
        )

    
    def computer_specifications(self):
        return (
            f'Сборка компьютера состоит из:\n'
            f'1. Материнская плата:\n'
            f'      Тип чипсета: {self.motherboard.socket_type}\n'
            f'      Кол-во слотов для RAM памяти: {self.motherboard.ram_slots} шт.\n'
            f'      Кол-во слотов для SSD памяти: {self.motherboard.ssd_slots} шт.\n'
            f'2. Блок питания:\n'
            f'      Мощность: {self.power_unit.max_power} Вт.\n'
            f'3. Процессор:\n'
            f'      Кол-во ядер: {self.cpu.cores} шт.\n'
            f'      Кол-во потоков: {self.cpu.cores*2} шт.\n'
            f'      Частота работы ядра: {self.cpu.processor_power} ГГц.\n'
            f'      Потребление: {self.cpu.energy_consumption} Вт.\n'
            f'4. Видеокарта:\n'
            f'      Модель: {self.video_card.video_model}\n'
            f'      Объем памяти: {self.video_card.video_memory} Гб.\n'
            f'      Потребление: {self.video_card.energy_consumption} Вт.\n'
            f'5. Оперативная память:\n'
            f'      Объем памяти (1 шт.): {self.ram.memory} Гб.\n'
            f'      Частота работы: {self.ram.frequency} МГц.\n'
            f'      Потребление(1 шт.): {self.ram.energy_consumption} Вт.\n'
            f'      Объем памяти с учетом возможности материнской платы ({self.motherboard.ram_slots} шт.): {self.motherboard.ram_slots*self.ram.memory} Гб.\n'
            f'      Потребление с учетом возможности материнской платы ({self.motherboard.ram_slots} шт.): {self.motherboard.ram_slots*self.ram.energy_consumption} Вт.\n'
            f'6. Встроенная память SSD:\n'
            f'      Объем памяти (1 шт.): {self.ssd.memory} Гб.\n'
            f'      Потребление (1 шт.): {self.ram.energy_consumption} Вт.\n'
            f'      Объем памяти с учетом возможности материнской платы ({self.motherboard.ssd_slots} шт.): {self.motherboard.ssd_slots*self.ssd.memory} Гб.\n'
            f'      Потребление с учетом возможности материнской платы ({self.motherboard.ssd_slots} шт.): {self.motherboard.ssd_slots*self.ssd.energy_consumption} Вт.\n'
            f'Сводка по энергопотреблению:\n'
            f'      Мощность от блока питания: {self.power_unit.max_power} Вт.\n'
            f'      Минимальная потребляемая мощьность: {self.sum_energy_consumption} Вт.\n'
            f'      Максимальная потребляемая мощьность: {self.max_sum_energy_consumption} Вт.\n'
        )
    
    def is_power_sufficient(self):
        """Проверяет, хватает ли мощности блока питания для работы системы."""
        return self.power_unit.max_power >= self.sum_energy_consumption
    
    def distribute_power(self):
        """Проверяет, может ли система работать на текущем уровне энергопотребления."""
        if not self.power_unit.state_power:
            print("Питание выключено. Включите блок питания.")
            return False
        
        if self.is_power_sufficient():
            print("Система работает нормально. Мощности достаточно.")
            return True
        else:
            print("Недостаточно мощности блока питания для работы системы.")
            return False
    
    def on_state_power(self):
        self.power_unit.on_state_power()
        if self.distribute_power():
            return True
        else:
            self.power_unit.off_state_power()
            return False
    
    def off_state_power(self):
        self.power_unit.off_state_power()
        self.off_display_image()
    
    def on_display_image(self):
        if self.power_unit.state_power:
            self.video_card.on_display_image()
        else:
            print(f'Для начала включите блок питания')
    
    def off_display_image(self):
        if self.power_unit.state_power:
            self.video_card.off_display_image()
        else:
            print(f'Питание отсутсвует, вывод изображения уже отсутсвует')
    
    def download_ram_data(self,ram_data):
        """ Сохраняем данные на RAM накопитель в массив """
        if self.power_unit.state_power:    
            self.ram.download_data(ram_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def remove_ram_data(self,ram_data):
        """ Удаляем данные c RAM накопитель в массив """
        if self.power_unit.state_power: 
            self.ram.remove_data(ram_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def download_ssd_data(self,ssd_data):
        """ Сохраняем данные на SSD накопитель в массив """
        if self.power_unit.state_power: 
            self.ssd.download_data(ssd_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def remove_ssd_data(self,ssd_data):
        """ Удаляем данные с SSD накопитель в массив """
        if self.power_unit.state_power: 
            self.ssd.remove_data(ssd_data)
        else:
            print(f'Питание отсутсвует, запись не возможна')
    
    def on_turbo_mode_cpu(self):
        if self.power_unit.state_power: 
            self.cpu.on_turbo_mode_cpu()
            if self.distribute_power():
                print(f'Потребление системы достаточно!')
                return True
            else:
                print(f'!Потребление системы не достаточно')
                return False
        else:
            print(f'Питание отсутсвует, опция недоступна')
    
    def off_turbo_mode_cpu(self):
        if self.power_unit.state_power: 
            self.cpu.off_turbo_mode_cpu()
            self.distribute_power()
        else:
            print(f'Питание отсутсвует, опция недоступна')


power_unit = PowerUnit(700)
motherboard = Motherboard('AM4', 4, 1)
cpu = Cpu(8,3.6,65)
ram = Ram(8,3600,5)
ssd = Ssd(1000, 5)
video_card = VideoCard('GeForce RTX 4060 Ti', 8, 500)

print('Вкл/Выкл трансляции изображения')
video_card.off_display_image()
video_card.on_display_image()
video_card.off_display_image()
print()

print('Сохранение и удаление на SSD')
ssd.download_data('Привет, Мир!')
ssd.download_data('Как дела, Мир?')
ssd.remove_data('Привет, Мир!')
ssd.remove_data('Как дела, Мир?')
ssd.remove_data('Nan')
print()

print('Сохранение и удаление на RAM')
ram.download_data('Привет, оперативка!')
ram.download_data('Как дела, оперативка?')
ram.remove_data('Привет, оперативка!')
ram.remove_data('Как дела, оперативка?')
ram.remove_data('Nan')
print()

power_unit.on_state_power()
power_unit.off_state_power()
print()

motherboard.distribute_power(800,5)
print()

cpu.on_turbo_mode_cpu()
cpu.off_turbo_mode_cpu()

print()
computer = Сomputer(power_unit, motherboard, cpu, ram, ssd, video_card)

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
computer.distribute_power()
computer.remove_ram_data('Привет, оперативка!')
computer.remove_ram_data('Привет!')
computer.download_ssd_data('Тук-Тук')
computer.remove_ssd_data('Привет!')
computer.remove_ssd_data('Тук-Тук')
computer.on_turbo_mode_cpu()
computer.off_turbo_mode_cpu()
