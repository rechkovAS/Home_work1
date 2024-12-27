# Задача "Range - это просто":

class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        """__init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
        # В этом методе в первую очередь проверяется step на равенство 0.
        # Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')"""
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.pointer = start
        self.i = 0


# Методы:

    def __iter__(self):
        """# __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора."""
        self.pointer = self.start
        return self


    def __next__(self):
        """# __next__ - метод, увеличивающий атрибут pointer на step.
        # В зависимости от знака атрибута step итерация завершится либо когда pointer станет больше stop,
        # либо меньше stop. Учтите это при описании метода."""
        self.i += 1
        if self.i > 1:
            self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        return self.pointer

# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1
# Примечания:
# Особое внимание уделите методу __next__ и условиям в нём.