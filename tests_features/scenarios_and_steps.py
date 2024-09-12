import pytest
from pytest_bdd import given, parsers, scenario, then, when

from test_task import MIN_DELIVERY_SUM, delivery_cost_calculation
from tests_features.steps_data import (
    distance_1,
    distance_2,
    distance_3,
    distance_4,
    fragile,
    high,
    increased,
    large,
    normal,
    small,
    standard,
    very_high,
)


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
        'standard': standard,
        'fragile': fragile,
        'distance_1': distance_1,
        'distance_2': distance_2,
        'distance_3': distance_3,
        'distance_4': distance_4,
        'small': small,
        'large': large,
        'normal': normal,
        'increased': increased,
        'high': high,
        'very high': very_high,
    }
    context = conditions_map[condition]
    return context

@when('Click to order button')
def when_click_to_order_button():


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
