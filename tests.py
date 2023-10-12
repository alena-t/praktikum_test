import pytest

from test_task import MIN_DELIVERY_SUM, delivery_cost_calculation


def test_type_of_output_params():
    distance = 10
    dimension = 'small'
    is_fragile = False
    workload = 'normal'
    assert type(delivery_cost_calculation(
        distance, dimension, is_fragile, workload)) == int, (
        "Итоговая сумма должна быть выведена в виде целого числа.")


def test_min_sum_of_delivery():
    distance = 10
    dimension = 'small'
    is_fragile = False
    workload = 'normal'
    assert delivery_cost_calculation(
        distance, dimension, is_fragile, workload) == MIN_DELIVERY_SUM, (
        "Сумма доставки не может быть меньше 400. "
        "Убедитесь, что соответствующее условие есть и описано правильно")


def test_exception_for_fragile_more_30_km():
    with pytest.raises(ValueError):
        delivery_cost_calculation(31, 'small', True, 'normal')
        pytest.fail(
            "Проверьте, что исключаете возможность перевозки "
            "грузов на расстояние более 30км")


def test_exception_for_unset_values():
    with pytest.raises(KeyError):
        delivery_cost_calculation(31, 'smally', None, 'normaly')
        pytest.fail(
            "Некорректное (ые) значения параметров. Проверьте, "
            "что используются только значения из описанных словарей")


@pytest.mark.parametrize('some_distance, result',
                         [(1, 400), (2, 420), (9, 420),
                          (10, 560), (29, 560), (30, 700), (31, 700)],
                         ids=[
                             'value_1_positive',
                             'value_1_positive',
                             'value_1_positive',
                             'value_1_positive',
                             'value_1_positive',
                             'value_1_negative',
                             'value_2_negative'
                         ])
def test_change_sum_from_distance(some_distance, result):
    distance = some_distance
    dimension = 'large'
    is_fragile = False
    workload = 'high'
    assert delivery_cost_calculation(
        distance, dimension, is_fragile, workload) == result, (
        "Сумма доставки рассчинтана неправильно. Убедитесь, что правильно "
        "указали диапозоны цен для изменения стоимости по расстоянию")


@pytest.mark.parametrize('some_dimension, result',
                         [('large', 560), ('small', 420)])
def test_change_sum_from_dimension(some_dimension, result):
    distance = 10
    dimension = some_dimension
    is_fragile = False
    workload = 'high'
    assert delivery_cost_calculation(
        distance, dimension, is_fragile, workload) == result, (
        "Сумма доставки рассчинтана неправильно. "
        "Убедитесь, что правильно обрабатываете случаи разных габаритов")


@pytest.mark.parametrize('some_workload, result',
                         [('normal', 700),
                          ('increased', 840),
                          ('high', 980),
                          ('very_high', 1120)])
def test_change_sum_from_workload(some_workload, result):
    distance = 10
    dimension = 'large'
    is_fragile = True
    workload = some_workload
    assert delivery_cost_calculation(
        distance, dimension, is_fragile, workload) == result, (
        "Сумма доставки рассчинтана неправильно. Убедитесь, что "
        "правильно обрабатываете случаи разной загруженности службы доставки")
