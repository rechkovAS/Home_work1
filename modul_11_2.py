import sys
from pprint import pprint
import inspect


# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
# Рекомендуется создавать свой класс и объект для лучшего понимания
# Файл с кодом прикрепите к домашнему заданию.
class Animal:
    live = True
    sound = None # - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0# - степень опасности существа
# Объект этого класса обладает следующими атрибутами:
    def __init__(self, speed):
        self._cords=[0, 0, 0]# - координаты в пространстве.
        self.speed = speed# - скорость передвижения существа (определяется при создании объекта)
# И методами:
    def move(self, dx, dy, dz):# move(self, dx, dy, dz), который должен менять соответствующие кооординаты в
                               # _cords на dx, dy и dz в том же порядке,
        if  dz * self.speed < 0: # Если при попытке изменения координаты z в _cords значение будет меньше 0,
                            # то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносяться.
            print(f"It's too deep, i can't dive {self.speed} :(")
            return self._cords
        else:
            self._cords[0] = dx * self.speed # где множетелем будет являтся speed.
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed
            return self._cords


    def get_cords(self):#выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self): #выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
                      # "Be careful, i'm attacking you 0_0" , если равно или больше.
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
    def speak(self): #который выводит строку со звуком sound.
        print(f'{self.sound}')
class Bird(Animal): #- класс описывающий птиц. Наследуется от Animal.
    beak = True# - наличие клюва
    def __init__(self, speed):
        super().__init__(speed)
    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")
class AquaticAnimal(Animal):# - класс описывающий плавающего животного. Наследуется от Animal.
    _DEGREE_OF_DANGER = 3 # В этом классе атрибут _DEGREE_OF_DANGER = 3.
    def dive_in(self, dz): #  - где dz изменение координаты z в _cords.
                           # Этот метод должен всегда уменьшать координату z в _coords.
                           # Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
                           # Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
        self._cords[2] = int(abs(dz / self.speed))
        return self._cords
class PoisonousAnimal(Animal):# - класс описывающий ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8.
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):# - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"# - звук, который издаёт утконос



def introspection_info(obj):
    i_i = {}
    i_i['тип объекта'] = type(obj)
    attrs_obj = []
    for attr in dir(obj):
        if hasattr(obj, attr):
            attrs_obj.append(attr)
    i_i['все атрибуты объекта'] = attrs_obj

    metods_obj = []
    for metod in dir(obj):
        if metod[0] == '_' and metod[1] == '_':
            metods_obj.append(metod)
    i_i['методы объекта'] = metods_obj
    # i_i['интерспективный анализ'] = inspect.getmembers(obj)
    i_i['модули'] = inspect.getmodule(obj)
    i_i['comments'] = inspect.getcomments(obj)
    i_i['doc'] = inspect.getdoc(obj)

    try:
        i_i['свойства и значения объекта'] = vars(obj)
    except TypeError as e:
        i_i['свойства и значения объекта'] = 'свойств и значений НЕ ИМЕЕТ'
    i_i['версия Python'] = sys.version.split(' ')[0]

    return i_i

db = Duckbill(10)
number_info = introspection_info(db)


pprint(number_info)