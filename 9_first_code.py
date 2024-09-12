from unittest.mock import Mock, patch


def some_func(arg):
    if arg == 2:
        return some_func_2(arg)
    else:
        return 2 + arg

class Some:

    def __init__(self):
        self.count = None


@patch('diplom.tests.some_func_file.TestClass.some_func_2')
@pytest.mark.parametrize(
    'result_value, result',
    [
        (2, 2),
        (3, 4)
    ]
)
def test_some_func(mock_some_func_2, result_value, result):
    mock_some_func_2.some_func_2.return_value = result_value
    mock_some_func_2.count = 0
    assert some_func(1) == result


if __name__ == '__main__':
    division(1, 0)
    division('1', '1')
    division(1, 1)
