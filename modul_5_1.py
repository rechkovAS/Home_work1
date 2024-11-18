# Задача "Developer - не только разработчик":
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        a = 1
        if new_floor < 1 or new_floor > int(self.number_of_floors):
            print("Такого этажа не существует")
        else:
            while a <= int(new_floor):
                print(a)
                a += 1

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
