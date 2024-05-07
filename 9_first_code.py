@property
def some(arg_1, arg_2, arg_3):
    if arg_1 > 1:
        print(True)
    if arg_2 == 2:
        print(False)
    if arg_3 < 3:
        print(True)
    print(False)


class Animal:
    tail = 1

    def __init__(self, name, date_of_birth=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.__head = 1
        self.result = {}

    def _eat(self, food_count):
        return f'{self.name} больше не голоден' if food_count >= 1 else f'{self.name} все еще голоден'

    @property
    def head(self):
        return self.__head

    @staticmethod
    def is_want_to_walking(hours):
        if hours > 3:
            return True
        return False

    @staticmethod
    def is_right_head_count(head_count):
        if head_count > 1:
            return 'Слишком много голов у животного!'
        return 'С головой все в порядке!'

    @classmethod
    def create_animal_with_validation(cls, name):
        if type(name) == str:
            return cls(name)
        return 'Имя должно быть строкой!'

    @classmethod
    def change_tail_count(cls, count):
        cls.tail = count


class Cat(Animal):
    tail = 2

    def say_something(self):
        print('Meow')


class Dog(Animal):
    tail = 0

    def say_something(self):
        print('Bark')


class MyException(Exception):

    def __init__(self, message, order):
        self.message = message
        self.order = order

    def __str__(self):
        return f'MyException: {self.message}'


def division(some_1: int, some_2: int):
    try:
        result = some_1/some_2
        raise MyException(
            'Что-то пошло не так!',
            'my_order'
        )
    except Exception:
        raise MyException(
            'Что-то пошло не так: некорретные данные переданы на вход',
            'my_order'
        )
    finally:
        print('1' + str(result))

# добавляем товар в чек
def add_item_to_cheque(self, name):
    if len(name) > 40:
        raise ValueError()
    elif name not in :
        raise NameError()
    else:
        self.__name_items.append(name)
        ...


if __name__ == '__main__':
    division(1, 0)
    division('1', '1')
    division(1, 1)
