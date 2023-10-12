
class Animal:

    def __init__(self, name):
        self.name = name
        self.__head = 1

    @property
    def head(self):
        return self.__head

    def eat(self, food_count):
        if food_count >= 1:
            print(f'{self.name} больше не голоден')
        else:
            print(f'{self.name} все еще голоден')

    @staticmethod
    def say_something(paws_count):
        if paws_count > 2:
            print('Это животное')
        else:
            print('Это птица!')

    @classmethod
    def create_cat_without_name(cls):
        name = 'Барсик Второй Шикарный'
        cls(name)


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.paws = 4
        self.tail = 1

    def say_something(self):
        print(f'{self.name} say Meow')

    def change_name(self, new_name):
        self.name = new_name


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.paws = 4
        self.tail = 1

    def _say_something(self):
        print(f'{self.name} говорит Гав')


def some_func(some_arg):
    try:
        result = 10 / some_arg
        result = result + 1
    except Exception as exc:
        print(f'Произошло исключение {exc}')
    finally:
        result = 10 * some_arg

    return result


def some_func_2(some_arg):
    if type(some_arg) in ['str', 'int']:
        print('ОК')
    raise TypeError('Некорректный тип аргумента')


if __name__ == '__main__':
    print(some_func('0'))

