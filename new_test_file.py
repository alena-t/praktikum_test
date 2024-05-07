from unittest.mock import patch

import pytest


def do_some():
    return 2 or 3

def do_some_1():
    var = do_something()
    return not var


@pytest.mark.parametrize(
    'some, result',
    [
        (1, 1),
        (2, 4),
        (3, 6)
    ]
)
@patch('selenium_testing.driver_settings.DoSomething')
def test_some_success(mock_do_something, some, result):
    mock_do_something.do_something.return_value = some
    assert do_some_1() == result
