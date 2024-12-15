import os
import time
print('Текущая директория:', os.getcwd())
# # file = [f for f in os.listdir() if os.path.isfile(f)]
# # print(file)
# # # os.startfile('test.txt')
# # # os.startfile(file[7])
# # print(os.stat('test.txt'))
# # import platform
# # system_info = platform.uname()
# # print(system_info)

#directory = r'C:\Users\Алексей\PycharmProjects\PythonProject_Modul_7'
directory = '.'

for root, dirs, files in os.walk(directory):#root, dirs, abspath
    for file in files:
        filepath = './' + os.path.join(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(os.getcwd())
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')
    # for roo in root:
    #     filepath = './' + os.path.join(roo)
    #     filesize = os.path.getsize(roo)
    #     print(f'Обнаружен файл: {roo}, Путь: {filepath}, Размер: {filesize} байт')

# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.