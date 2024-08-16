import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration


class UrTube:
    current_user = None

    def __init__(self):
        self.users = {}
        self.user_age = {}
        self.videos = []

    def log_in(self, nickname, password):
        if nickname in self.users and password in self.users:
            UrTube.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')

        else:
            self.users[nickname] = password
            self.user_age[nickname] = age
            UrTube.current_user = nickname

    @staticmethod
    def log_out(self):
        ur.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word):
        if search_word in self.videos:
            print(self.videos)
    # Никак не соображу как в get_videos из self.videos достать title.
    # Или функцию add нужно по другому прописать?

    def watch_video(self, movie_title):
        if ur.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')

        elif ur.user_age[ur.current_user] < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif movie_title in self.videos:
            time.sleep(Video)
            print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print()
