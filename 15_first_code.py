import pytest
from selenium.webdriver.common.by import By


class MyCastomException(Exception):

    def __init__(self, message):
        self.message = message
        self.code = 400

    def __str__(self):
        return f'MyCastomException: {self.message}, {self.code}'


def division(arg_1, arg_2):
    try:
        result = arg_1/arg_2
    except (ZeroDivisionError, TypeError):
        raise MyCastomException('value not good')
    # finally:
    #     result = result + 1

    return result

def some_func(arg):
    if arg > 2:
        raise MyCastomException('value too big')
    return arg + 1

@pytest.mark.parametrize(
        'question_locator, answer_locator, answer_text',
        [
            [(By.XPATH, '//*[@id="accordion__heading-0"]'), (By.ID, "accordion__panel-0"), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']
        ]
    )


if __name__ == '__main__':
    print(division(1, 2))
    print(division(4, 2))
    print(division(5, 0))
    # print(division(5, 1))
    # print(division(5, '1'))
    print(some_func(1))
    print(some_func(3))
