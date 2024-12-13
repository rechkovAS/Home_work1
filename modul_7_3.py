import io
from pprint import pprint
# Задача "Найдёт везде":
class WordsFinder:
    def __init__(self, *file_names: list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text_file_all = file.read().lower()
                example_table = {ord('$'): ' ', ord('%'): ' ', ord(','): ' ', ord('.'): ' ', ord('='): ' ',
                                 ord('!'): ' ', ord('?'): ' ', ord(';'): ' ', ord(':'): ' '}
                text_file = text_file_all.translate(example_table)
                text_file2 = text_file.replace(' - ', '')
                world_file = text_file2.split()
                all_words[file_name] = world_file
        return all_words

    def find(self, word):
        """count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - количество слова word в списке слов этого файла. В методах find и count пользуйтесь ранее
        написанным методом get_all_words для получения названия файла и списка его слов.
        """
        position_words = {}
        for file_name, world_file in self.get_all_words().items():
            word_lower = word.lower()
            for number in range(len(world_file)):
                position_number = 0
                if world_file[number] == word_lower:
                    position_number = number + 1
                    break
            position_words[file_name] = position_number

        # all_words = list(self.get_all_words().items())
        # # print(all_words)
        # for i in range(len(all_words)):
        #     file_name = all_words[i][0]
        #     world_file = all_words[i][1]
        return position_words
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
#     def count(self, word):
#         count_words = {}
#         all_words = list(self.get_all_words().items())
#         # print(all_words)
#         for i in range(len(all_words)):
#             file_name = all_words[i][0]
#             world_file = all_words[i][1]
#             word_lower = word.lower()
#             quantity = 0
#             for number in range(len(world_file)):
#                 if world_file[number] == word_lower:
#                     quantity += 1
#
#             count_words[file_name] = quantity
#
#         return count_words
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
    def count(self, word):
        """# for name, words in get_all_words().items():"""
        count_words = {}
        for file_name, world_file in self.get_all_words().items():
            word_lower = word.lower()
            quantity = 0
            for number in range(len(world_file)):
                if world_file[number] == word_lower:
                    quantity += 1

            count_words[file_name] = quantity

        return count_words


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt', 'products.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

