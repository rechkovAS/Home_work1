# Задача "Потоки гостей в кафе":
import queue
import random
import threading
import time


class Table:
    """Table - стол, хранит информацию о находящемся за ним гостем (Guest)
    Объекты этого класса должны создаваться следующим способом - Table(1). Обладать атрибутами number - номер стола
     и guest - гость, который сидит за этим столом (по умолчанию None)
    """
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    """Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
    Должен наследоваться от класса Thread (быть потоком). Объекты этого класса должны создаваться
    следующим способом - Guest('Vasya'). Обладать атрибутом name - имя гостя. Обладать методом run, где происходит
    ожидание случайным образом от 3 до 10 секунд.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    """Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
    и их обслуживания (discuss_guests). Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
    Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    """
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        """Должен принимать неограниченное кол-во гостей (объектов класса Guest). Далее, если есть свободный стол,
        то сажать гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку
        "<имя гостя> сел(-а) за стол номер <номер стола>". Если же свободных столов для посадки не осталось,
        то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
        """

        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """метод имитирует процесс обслуживания гостей. Обслуживание должно происходить пока очередь не пустая
        (метод empty) или хотя бы один стол занят. Если за столом есть гость(поток) и гость(поток) закончил приём пищи
        (поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и
        ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
        Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу
        присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла)
        из очереди и сел(-а) за стол номер <номер стола>". Далее запустить поток этого гостя (start)
        """
        while not self.queue.empty() or any([True if not table.guest is None else False for table in self.tables]):#
           for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()

# # Создание столов
tables = [Table(number) for number in range(1, 6)]
# # Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
