# Задача "Изменять нельзя получать":
# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.
# I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(f"{self.get_model()}, {self.get_horsepower()}, {self.get_color()}, Владелец: {self.owner} ")
        # Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
        # если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        # "Нельзя сменить цвет на <новый цвет>".
    def set_color(self, new_color):
        x = new_color.lower()
        y = [i.lower() for i in self.__COLOR_VARIANTS]
        # print(x)
        # print(y)
        # #new_color = new_color.upper
        if x in y:
        #if isinstance(x, tuple(i.lower() for i in self.__COLOR_VARIANTS)):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Взаимосвязь методов и скрытых атрибутов:
# Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
# __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
# Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

# Пример результата выполнения программы:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok