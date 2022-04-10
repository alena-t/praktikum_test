delivery_distance = {
    'more_30': 300,
    'less_30': 200,
    'less_10': 100,
    'less_2': 50,
}

dimensions = {
    'large': 200,
    'small': 100,
}

workload_ratio = {
    'very_high': 1.6,
    'high': 1.4,
    'increased': 1.2,
    'normal': 1,
}

MIN_DELIVERY_SUM = 400


def get_cost_from_distance(distance: float) -> float:
    """Implement the logic for choosing
    delivery costs relative to distance."""
    if distance >= 30:
        return delivery_distance['more_30']
    elif 30 > distance >= 10:
        return delivery_distance['less_30']
    elif 10 > distance >= 2:
        return delivery_distance['less_10']
    return delivery_distance['less_2']


def delivery_cost_calculation(
        distance: float,
        dimension: str,
        is_fragile: bool,
        workload: str) -> int:
    """Implement the logic for calculating
    the final cost of delivery."""
    fragile_cost = 0
    if is_fragile is True:
        if distance > 30:
            raise ValueError(
                'Хрупкие грузы нельзя возить на расстояние, превышающее 30 км!'
            )
        else:
            fragile_cost = 300
    distance_cost = get_cost_from_distance(distance)
    dimension_cost = dimensions[dimension]
    workload_cost = workload_ratio[workload]
    final_cost = distance_cost + dimension_cost + fragile_cost
    final_cost = final_cost * workload_cost
    if final_cost < MIN_DELIVERY_SUM:
        return MIN_DELIVERY_SUM
    return round(final_cost)


if __name__ == '__main__':
    distance = 10
    dimension = 'large'
    is_fragile = True
    workload = 'very_high'
    print(delivery_cost_calculation(distance, dimension, is_fragile, workload))
