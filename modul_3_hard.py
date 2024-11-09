
summa = 0
def calculate_structure_sum(*args):
    global summa
    for i in args:
        if isinstance(i, int):
            summa += i
            print(summa, f'результат после прибавления числа {i}')
        elif isinstance(i, str):
            summa += len(i)
            print(summa, 'str')
        elif isinstance(i, tuple):
            for j in i:
                if isinstance(j, int):
                    summa += j
                    print(summa, f'результат после прибавления числа {j}')
                elif isinstance(j, str):
                    summa += len(j)
                    print(summa, f'результат после прибавления {len(j)} символов от строки: {j}')
                elif isinstance(j, tuple):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления картежа {j}')
                elif isinstance(j, list):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления списка {j}')
                elif isinstance(j, dict):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления словаря {j}')
                elif isinstance(j, set):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления множества {j}')

        elif isinstance(i, list):
            for j in i:
                if isinstance(j, int):
                    summa += j
                    print(summa, f'результат после прибавления числа {j}')
                elif isinstance(j, str):
                    summa += len(j)
                    print(summa, f'результат после прибавления {len(j)} символов от строки: {j}')
                elif isinstance(j, tuple):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления картежа {j}')
                elif isinstance(j, list):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления списка {j}')
                elif isinstance(j, dict):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления словаря {j}')
                elif isinstance(j, set):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления множества {j}')
        elif isinstance(i, dict):
            i = i.items()
            for j in i:
                if isinstance(j, int):
                    summa += j
                    print(summa, f'результат после прибавления числа {j}')
                elif isinstance(j, str):
                    summa += len(j)
                    print(summa, f'результат после прибавления {len(j)} символов от строки: {j}')
                elif isinstance(j, tuple):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления картежа {j}')
                elif isinstance(j, list):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления списка {j}')
                elif isinstance(j, dict):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления словаря {j}')
                elif isinstance(j, set):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления множества {j}')
        elif isinstance(i, set):
            i = list(i)
            for j in i:
                if isinstance(j, int):
                    summa += j
                    print(summa, f'результат после прибавления числа {j}')
                elif isinstance(j, str):
                    summa += len(j)
                    print(summa, f'результат после прибавления {len(j)} символов от строки: {j}')
                elif isinstance(j, tuple):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления картежа {j}')
                elif isinstance(j, list):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления списка {j}')
                elif isinstance(j, dict):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления словаря {j}')
                elif isinstance(j, set):
                    calculate_structure_sum(j)
                    print(summa, f'результат после прибавления множества {j}')

    return summa

# Входные данные (применение функции):
data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)

print(f'Ответ задачи: {result}')
