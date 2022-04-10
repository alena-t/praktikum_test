import pytest
from pytest_bdd import given, parsers, then, scenario

from test_task import delivery_cost_calculation, MIN_DELIVERY_SUM


@scenario("test_for_test_task.feature", "Min sum of delivery")
def test_min_sum():
    pass


@scenario("test_for_test_task.feature", "Fragile more 30 km")
def test_fragile_sum():
    pass


@scenario("test_for_test_task.feature", "Change sum for distance")
def test_distance_sum():
    pass


@scenario("test_for_test_task.feature", "Change sum for dimension")
def test_dimension_sum():
    pass


@scenario("test_for_test_task.feature", "Change sum for workload")
def test_dimension_workload():
    pass


@pytest.fixture
def context_dict():
    return {}


@given(parsers.parse('I have {condition} delivery terms'), target_fixture="context_dict")
def given_step(condition):
    conditions_map = {
        'standard': {'distance': 10,
                     'dimension': 'small',
                     'is_fragile': False,
                     'workload': 'normal'},
        'fragile': {'distance': 31,
                    'dimension': 'small',
                    'is_fragile': True,
                    'workload': 'normal'},
        'distance_1': {'distance': 1,
                       'dimension': 'large',
                       'is_fragile': False,
                       'workload': 'high'},
        'distance_2': {'distance': 2,
                       'dimension': 'large',
                       'is_fragile': False,
                       'workload': 'high'},
        'distance_3': {'distance': 10,
                       'dimension': 'large',
                       'is_fragile': False,
                       'workload': 'high'},
        'distance_4': {'distance': 30,
                       'dimension': 'large',
                       'is_fragile': False,
                       'workload': 'high'},
        'small': {'distance': 10,
                  'dimension': 'small',
                  'is_fragile': False,
                  'workload': 'high'},
        'large': {'distance': 10,
                  'dimension': 'large',
                  'is_fragile': False,
                  'workload': 'high'},
        'normal': {'distance': 10,
                   'dimension': 'large',
                   'is_fragile': True,
                   'workload': 'normal'},
        'increased': {'distance': 10,
                      'dimension': 'large',
                      'is_fragile': True,
                      'workload': 'increased'},
        'high': {'distance': 10,
                 'dimension': 'large',
                 'is_fragile': True,
                 'workload': 'high'},
        'very high': {'distance': 10,
                      'dimension': 'large',
                      'is_fragile': True,
                      'workload': 'very_high'},
    }
    context = conditions_map[condition]
    return context


@then('I see min sum of delivery')
def then_for_min_price(context_dict):
    distance = context_dict.get('distance')
    dimension = context_dict.get('dimension')
    is_fragile = context_dict.get('is_fragile')
    workload = context_dict.get('workload')
    assert delivery_cost_calculation(
        distance, dimension, is_fragile, workload) == MIN_DELIVERY_SUM, (
        "Сумма доставки не может быть меньше 400. "
        "Убедитесь, что соответствующее условие есть и описано правильно"
    )


@then('I see delivery is not possible')
def not_possible_delivery(context_dict):
    distance = context_dict.get('distance')
    dimension = context_dict.get('dimension')
    is_fragile = context_dict.get('is_fragile')
    workload = context_dict.get('workload')
    with pytest.raises(ValueError):
        delivery_cost_calculation(distance, dimension, is_fragile, workload)
        pytest.fail(
            "Проверьте, что исключаете возможность перевозки "
            "грузов на расстояние более 30км")


@then(parsers.parse('I see delivery sum is right for {result}'))
def sum_of_delivery_from_distance(context_dict, result):
    results_map = {
        'sum_1': 400,
        'sum_2': 420,
        'sum_3': 560,
        'sum_4': 700,
        'sum_5': 840,
        'sum_6': 980,
        'sum_7': 1120,
    }
    distance = context_dict.get('distance')
    dimension = context_dict.get('dimension')
    is_fragile = context_dict.get('is_fragile')
    workload = context_dict.get('workload')
    assert delivery_cost_calculation(
        distance, dimension, is_fragile, workload) == results_map[result], (
        "Сумма доставки рассчинтана неправильно. "
        "Убедитесь, что: \n - выводите сумму в виде целого числа"
        " \n - правильно указали диапозоны цен для изменения стоимости по расстоянию")
