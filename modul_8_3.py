
# Задача "Некорректность":

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



class Car:
    def __init__(self, model, __vin, numbers):
        self.model = model
        self. __vin = __vin
        self.__numbers = numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        """Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
         если передано не целое число. Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
         если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
         Возвращает True, если исключения не были выброшены.
         """
        if not isinstance(vin_number, int):
            print(isinstance(vin_number, int))
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, number):
        """Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        если передана не строка.(тип данных можно проверить функцией isinstance).
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна
        состоять ровно из 6 символов. Возвращает True, если исключения не были выброшены.
        """
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not len(number) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True
try:

  first = Car('Model1', 1000000, 'f123dj')

except IncorrectVinNumber as exc:

  print(exc.message)

except IncorrectCarNumbers as exc:

  print(exc.message)

else:

  print(f'{first.model} успешно создан')



try:

  second = Car('Model2', 300, 'т001тр')

except IncorrectVinNumber as exc:

  print(exc.message)

except IncorrectCarNumbers as exc:

  print(exc.message)

else:

  print(f'{second.model} успешно создан')



try:

  third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:

  print(exc.message)

except IncorrectCarNumbers as exc:

  print(exc.message)

else:

  print(f'{third.model} успешно создан')


