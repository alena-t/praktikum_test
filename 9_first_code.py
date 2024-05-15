import pytest

class Cat:

    def __init__(self):  # конструктор, который инициализирует пустую коллекцию фильмов
        self.movies = []

    def add_movie(self, name, year,
                  rating):  # метод добавляет фильм в коллекцию. Создает в списке новый объект с ключами: имя, год, рейтинг

        self.movies.append({"name": name,  # добавляет созданный объект в список фильмов
                            "year": year,
                            "rating": rating})

    def get_movies_by_year(self, year):

        def filter_func(some_element):
            return some_element['year'] == year

        movies_by_year = list(filter(filter_func,
                                     self.movies))

        return movies_by_year


def print_something(arg):
    if 0 <= arg < 2:
        return 'some from 0 to 2'
    elif 2 <= arg < 5:
        return 'some from 2 to 5'
    return 'some else'


class TestClass:

    @pytest.mark.parametrize(
        'arg, result',
        [
            (1, 'some from 0 to 2'),
            (2, 'some from 2 to 5'),
            (6, 'some else 1')
        ],
        ids=[
            'Test for 1',
            'Test for 2',
            'Test for 6'
        ]
    )
    def test_print_something(self, arg, result):
        some = print_something(arg)
        assert some == result, (
            f'Результат не соответствует ожидаемому {some} != {result}'
        )
