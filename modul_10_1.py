# Задача "Потоковая запись в файлы":

import threading
import time
def write_words(word_count, file_name):
    started_at = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    ended_at = time.time()
    elapsed = round(ended_at - started_at)
    print(f'Завершилась запись в файл {file_name} в {ended_at}. Функция работала {elapsed} секунд(ы)')

started_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = time.time()
elapsed = round(ended_at - started_at)
print(f'Завершилась запись в файлы в один поток за  {elapsed} секунд(ы)')


started_at = time.time()
write_words_5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
write_words_6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
write_words_7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
write_words_8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
write_words_5.start()
write_words_6.start()
write_words_7.start()
write_words_8.start()
write_words_5.join()
write_words_6.join()
write_words_7.join()
write_words_8.join()
ended_at = time.time()
elapsed = round(ended_at - started_at)
print(f'Завершилась запись в файлы в один поток за  {elapsed} секунд(ы)')
