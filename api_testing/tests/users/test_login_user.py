from unittest.mock import Mock, patch


def some_func():
    result = say_meaw()
    if result == 'Котик говорит мяу':
        return 1
    return 0


class TestClass:


    # @patch(
    #     'api_testing.tests.couriers.test_create_courier.TestBun',
    #
    # )
    @patch(
        'api_testing.practikum.bun.Bun.',
    )
    def test_check_burger_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, "Бургер состоит из неправильных булок!"

    def test_burger(self, burger):
        database = Database()
        buns = database.available_buns()
        bun = choice(buns)
        ingredients = database.available_ingredients()
        ingredient = choice(ingredients)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == bun.get_price() * 2 + ingredient.get_price() and 1==1, (
            f"Стоимость бургера {burger.get_price()} некорректная или {bun.get_price()}!"
        )

class SomeResp(BaseModel):
    price: int
    name: str
    type: str
    same_ingredients: list[Ingredient]

    {
        'price': 100,
        'name': '',
        'same_ingredients': [{
            'name': '',
            'type': 10
        }]
    }

