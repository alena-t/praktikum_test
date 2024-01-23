import time

# чтобы ничего не отвлекало,
# в классе реализованы только два метода
class User:

    def __init__(self):
        self.photo = None

    def upload_photo(self, photo):
        self.photo = photo
        time.sleep(30)  # имитируем медленную работу метода
        return 'OK'

    def create_user_profile(self, photo_path):   # создаём профиль пользователя
        result = self.upload_photo(photo_path)
        if result == 'OK':
            return 'Профиль создан'
        else:
            return 'Не удалось создать профиль'