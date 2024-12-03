import time

class User:
    """Пользователи"""
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.list_nickname = []

    def __hash__(self):
        return hash(self.password)

    def __eq__(self, other):
        return self.nickname == other.nickname
    def __repr__(self):
        return f'{self.nickname}'
class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f'{self.title}'

class UrTube:

    def __init__(self):
        self.users = [] # список объектов User
        self.videos = [] # список объектов Video
        self.current_user = None # текущий пользователь, User

    def log_in(self, nickname, password):
        """Метод log_in принимает на вход аргументы: nickname, password и пытается найти пользователя в users
         с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
         Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        control_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == control_password:
                self.current_user = user
                return print(f"Пользователь {nickname} вошёл в систему.")
        return print("Ошибка входа: неверный логин или пароль.")

    def register(self, nickname, password, age):
        """
        Метод register принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None."""
        self.current_user = None
        return print('Пользователь вышел!')

    def add(self, *args):
        """Метод add принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит."""
        if args not in self.videos:
            self.videos += args
        return self.videos



# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    def get_videos(self, search_engine):
        """  Метод get_videos принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
            Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        """
        search_result = []
        x = search_engine.lower()
        for video in self.videos:
            if x in video.title.lower():
                search_result.append(video.title)
        return search_result

    def watch_video(self,name_film):
        """Метод watch_video принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео" """
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for video in self.videos:
                if name_film == video.title:
                    for second in range(video.time_now + 1, video.duration + 1):
                        print(second, end=' ', flush=True)
                        time.sleep(1)
                    print("Конец видео")
                    video.time_now = 0




ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# # Добавление видео
ur.add(v1, v2)
# # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist