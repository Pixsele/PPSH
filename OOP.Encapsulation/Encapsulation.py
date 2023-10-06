import datetime
import random


class Emerald:
    # список статусов
    __status_massive = ['Не учтен', 'Учтен', 'Отправлен под спуд']

    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0

        # цена изумруда
        self.__price = 0

    def __str__(self):
        return f'Status : {self.__status_massive[self.__status]}, price : {self.__price}'

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, number):
        self.__status = number

    def account(self):
        if self.status < 1:
            self.status = 1
        else:
            raise ValueError('Object has already been account')

    def store(self):
        if self.status < 2:
            self.status = 2
        else:
            raise ValueError('Object has already been store')

    def set_price(self, new_price):
        self.__price = new_price


class Shell:
    # список статусов
    __status_massive = ['Не учтена', 'Учтена', 'Отправлена в монетолитейное отделение', 'Переплавлена в монету']

    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0

        # цена скорлупки
        self.__price = 0

    def __str__(self):
        return f'Status : {self.__status_massive[self.__status]}, price : {self.__price}'

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, number):
        self.__status = number

    def account(self):
        if self.status < 1:
            self.status = 1
        else:
            raise ValueError('Object has already been account')

    def process(self):
        if self.status < 2:
            self.status = 2
        else:
            raise ValueError('Object has already been process')

    def smelt(self, archive, value=0):
        if self.status < 3:
            archive.add(Coin(value))
            self.__status = 3
        else:
            raise ValueError('Object has already been smelt')

    def set_price(self, new_price):
        self.__price = new_price


class Coin:
    __current_serial_number = 0

    def __init__(self, value=0):
        # серийный номер монеты
        self.__serial_number = self.__create_new_serial_number()
        # год выпуска монеты
        self.__year = self.__get_current_year()
        # номинал монеты
        if value == 0:
            self.__value = self.__set_random_value()
        else:
            self.__value = value

    def __str__(self):
        return f'Serial number : {self.get_serial_number()} , Year : {self.get_year()}, Value : {self.get_value()}'

    def get_serial_number(self):
        return self.__serial_number

    def get_year(self):
        return self.__year

    def get_value(self):
        return self.__value

    @staticmethod
    def __create_new_serial_number():
        new_serial_number = Coin.__current_serial_number + 1
        Coin.__current_serial_number = new_serial_number
        return new_serial_number

    @staticmethod
    def __get_current_year():
        return datetime.date.today().year

    @staticmethod
    def __set_random_value():
        return random.choice([1, 2, 5, 10])


class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []

    def __str__(self):
        result = f'Объектов в архиве : {len(self.__storage)}\n'
        for index in range(len(self.__storage)):
            result += f'{str(self.__storage[index])}\n'
        return result

    def add(self, new_entry):
        self.__storage.append(Entry(new_entry))

    def archive(self, index):
        if self.__storage[index] != None:
            return self.__storage[index].show_object_info()
        else:
            return 'None'

    def delete_entry(self, index):
        if self.__storage[index] != None:
            self.__storage[index] = None
        else:
            raise IndexError('Object already is None')

    def change_entry_info(self, index, new_info):
        if self.__storage[index] != None:
            self.__storage[index].change_object_info(new_info)
        else:
            raise IndexError('Object is None')

    def change_entry_secret_type(self, index):
        if self.__storage[index] != None:
            self.__storage[index].change_secret_type()
        else:
            raise IndexError('Object is None')


class Entry:
    def __init__(self, item, info='', secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()

        # указатель на объект
        self.__item = item

        # дата создания записи
        self.__date = self.__get_current_date()

        # дополнительная информация об объекте
        self.__info = info

        # информация засекречена?
        self.__secret = secret

    def __str__(self):
        return f'Type object : {self.__item.__class__.__name__} , date : {self.__date}, info : {self.__info}, secret? = {self.__secret}, {str(self.__item)}'

    def change_secret_type(self):
        if self.__secret == True:
            self.__secret = False
        else:
            self.__secret = True

    def change_object_info(self, new_info):
        self.__info = new_info

    def show_object_info(self):
        if self.__secret == True:
            return None
        else:
            return f'Type object : {self.__item.__class__.__name__} , date : {self.__date}, info : {self.__info}, {str(self.__item)}'

    def __get_next_ID(self):
        return hash(self)

    @staticmethod
    def __get_current_date():
        return str(datetime.date.today())


# Создание архива
myarchive = Archive()
# Создание и учёт в архиве изумрудов и скорлупок
emeralds = [Emerald() for i in range(10)]
shells = [Shell() for i in range(20)]
for i in range(20):
    myarchive.add(shells[i])
for i in range(10):
    myarchive.add(emeralds[i])
print('Создание и учёт в архиве изумрудов и скорлупок\n', myarchive)
# Изменение статуса изумрудов и скорлупок
for i in range(10):
    emeralds[i].store()
for i in range(20):
    shells[i].process()
print('Изменение статуса изумрудов и скорлупок\n', myarchive)
# Переплавка монет
for i in range(20):
    shells[i].smelt(myarchive)
print('Переплавка монет\n', myarchive)
# Засекречивание записией об изумрудах
for i in range(20, 30):
    myarchive.change_entry_secret_type(i)
print('Засекречивание записией об изумрудах\n', myarchive)
# Удаление записей о скорлупках
for i in range(20):
    myarchive.delete_entry(i)
print('Удаление записей о скорлупках\n', myarchive)
# Рассекречивание записией об изумрудах
for i in range(20, 30):
    myarchive.change_entry_secret_type(i)
print('Рассекречивание записией об изумрудах\n', myarchive)
# Изменение информации об изумруде
for i in range(20, 30):
    myarchive.change_entry_info(i, 'super duper info')
print('Изменение информации об изумруде\n', myarchive)
# Рассекречивание части записей об изумрудах
for i in range(20, 25):
    myarchive.change_entry_secret_type(i)
print('Рассекречивание части записей об изумрудах\n', myarchive)
# Доп.инфа к рассекреченным изумрудам
for i in range(20, 25):
    myarchive.change_entry_info(i, 'secret info')
print('Доп.инфа к рассекреченным изумрудам\n', myarchive)
# Получние информации о монетах
print('Получние информации о монетах\n')
for i in range(30, 50):
    print(myarchive.archive(i))
