
class Animal:

    def __init__(self, name):
        self.name = name
        self._head = 1

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
        self.__tail = 1

    def _say_something(self):
        print(f'{self.name} говорит Гав')

    @property
    def tail(self):
        return self.__tail

    def division(self, num):
        try:
            result = self.paws / num
        except ZeroDivisionError:
            result = 'Нельзя делить на 0'
        finally:
            result_1 = 'Это выход из программы, не уверены, что все хорошо'

        return result, result_1



if __name__ == '__main__':
    cat = Cat('Барсик')
    animal = Animal('Кто-то')
    dog = Dog('Рекс')
    print(dog.division(4))

