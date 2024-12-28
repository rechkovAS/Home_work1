
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        control = 0
        for i in range(2, result):
            if result % i == 0:
                control += i
        if control == 0:
            print("Простое")
        return result
    return wrapper



@is_prime
def sum_three(first, second, third):
    sum_3 = first + second + third
    return sum_3


# Пример:
result = sum_three(2, 3, 6)
print(result)
