from selenium.webdriver.common.devtools.v85.debugger import resume


class WrongDriverException(Exception):

    def __init__(self, driver_name):
        self.driver_name = driver_name


    def __str__(self):
        return f'{self.driver_name} driver do not support Chrome browser'


def some_test_func(arg):

    if arg > 0:
        return arg / 10
    elif arg < 0:
        return 10 / arg

    raise WrongDriverException(
        driver_name='ff'
    )


if __name__ == '__main__':

    print(some_test_func(3))
    print(some_test_func(0))


