import multiprocessing
import datetime

def read_info(name):
    """Создаёт локальный список all_data. Открывает файл name для чтения.
    Считывает информацию построчно (readline), пока считанная строка не окажется пустой.
    Во время считывания добавляет каждую строку в список all_data.
    """
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            x = file.readline()
            if not x:
                break
            all_data.append(x.strip())

filenames = [f'file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов
    start = datetime.datetime.now()
    list(map(read_info, filenames))
    end = datetime.datetime.now()
    print(end - start, '- линейный')

    # Многопроцессный
    start = datetime.datetime.now()
    p = multiprocessing.Pool()
    with p:
        p.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start, '- многопроцессный')



# Вывод на консоль, 2 запуска (результаты могут отличаться):
# 0:00:03.046163 (линейный)
# 0:00:01.092300 (многопроцессный)
