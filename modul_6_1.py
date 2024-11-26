# Задача "Съедобное, несъедобное":
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
class Animal:
    alive = True #живой
    fed = False #накормленный
    def __init__(self, name):
        self.name = name

    # Метод eat должен работать следующим образом:
    # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
    # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
    def eat(self, food):
        if food.edible == True:
            print(f'<{self.name}> съел <{food.name}>')
            Animal.fed = True
        else:
            print(f'<{self.name}> не стал есть <{food.name}>')
            Animal.alive = False

# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
class Plant:
    edible = False #(съедобность)
    def __init__(self, name):
        self.name = name

# 4 класса наследника: # Mammal, Predator для Animal.
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
class Mammal(Animal):
        pass

class Predator(Animal):
        pass
# Flower, Fruit для Plant.
class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

# В данном случае можно использовать принцип наследования, чтобы не дублировать код.

# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
# Пункты задачи:
# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами. При необходимости переопределите значения атрибутов.
# Создайте объекты этих классов.
# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
