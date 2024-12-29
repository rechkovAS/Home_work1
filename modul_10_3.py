# Задача "Банковские операции":
import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        """Будет совершать 100 транзакций пополнения средств. Пополнение - это увеличение баланса на случайное целое
        число от 50 до 500. Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(),
        то разблокировать его методом release. После увеличения баланса должна выводится строка "Пополнение:
        <случайное число>. Баланс: <текущий баланс>". Также после всех операций поставьте ожидание в 0.001 секунды,
        тем самым имитируя скорость выполнения пополнения.
        """
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = random.randint(50, 500)
            self.balance += x
            print(f'{i}Пополнение: {x}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        """Будет совершать 100 транзакций снятия. Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
        В начале должно выводится сообщение "Запрос на <случайное число>".
        Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие,
        уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
        Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и
        заблокировать поток методом acquiere.
        """
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'{i}Снятие: {x}. Баланс: {self.balance}')

            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')


