
# Задача "Записать и запомнить":


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    number_str = 0
    for string in strings:
        number_str += 1
        strings_positions[(number_str, file.tell())] = string
        # strings_positions.update{(number_str, file.tell()): string}
        file.write(f'{string}\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
