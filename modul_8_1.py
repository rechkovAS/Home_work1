# Задание "Программистам всё можно":
def add_everything_up(a: (int, float, str), b: (int, float, str)):
    """принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    TypeError - когда a и b окажутся разными типами (числом и строкой),
    то возвращать строковое представление этих двух данных вместе (в том же порядке).
    Во всех остальных случаях выполнять стандартные действия.
    """
    try:
        return a + b
    except TypeError:
        return f'{a}{b}'


# Пример кода:
print(add_everything_up(123.456, 'строка'))

print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('яблоко', 'строка'))
