# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # def go_to(self, new_floor):
    #     self.new_floor = int(new_floor)
    #     a = 1
    #     if new_floor < 1 or new_floor > int(self.number_of_floors):
    #         print("Такого этажа не существует")
    #     else:
    #         while a <= int(new_floor):
    #             print(a)
    #             a += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

