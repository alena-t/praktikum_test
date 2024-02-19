import datetime


class MyException(Exception):
    pass


def some_test_func(num):
    try:
        result = 10 / num
        raise ZeroDivisionError
    except ZeroDivisionError:
        raise MyException


today = datetime.datetime.now()
hours = today.time().hour
hours = today.time().strftime('%H') + 'h'


if __name__ == '__main__':
    print(some_test_func(1))
    print(some_test_func(0))
    print(some_test_func(2))
