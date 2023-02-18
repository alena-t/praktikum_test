import re
from enum import Enum

import pyparsing
from pyparsing import Regex


class MealDays(str, Enum):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'


class MealTime(str, Enum):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'


class MealType(str, Enum):
    VEGETARIAN = 'vegetarian'
    STANDARD = 'standard'
    CHILDISH = 'childish'


MEAL_DAYS_MAPPING = {
    'ПН': MealDays.MONDAY,
    'ВТ': MealDays.TUESDAY,
    'СР': MealDays.WEDNESDAY,
    'ЧТ': MealDays.THURSDAY,
    'ПТ': MealDays.FRIDAY,
    'СБ': MealDays.SATURDAY,
    'СУБ': MealDays.SATURDAY,
    'ВС': MealDays.SUNDAY,
    'ВСК': MealDays.SUNDAY,
}

MEAL_TYPE_MAPPING = {
    'ДЕТСКИЙ': MealType.CHILDISH,
    'СТАНДАРТ': MealType.STANDARD,
    'ВЕГЕТАРИАНСКИЙ': MealType.VEGETARIAN
}

EXCLUDED_DISHES = ['ПЛОВ', 'БИФСТРОГАНОВ', 'БИФ.СТРОГАНОВ', 'БИФ-СТРОГАНОВ']

string_for_parse = '1 РАЦИОН (ПН, СР, ПТ, ВСК.): НАРЕЗКА СЫРНАЯ, ОМЛЕТ С ПАПРИКОЙ, СОК, КОНДИТЕРСКОЕ ИЗДЕЛИЕ, БУЛОЧКА ПШЕНИЧНАЯ. 2 РАЦИОН (ВТ, ЧТ., СУБ.): НАРЕЗКА ОВОЩНАЯ, КАША РИСОВАЯ МОЛОЧНАЯ С ДЖЕМОМ, СОК, КОНДИТЕРСКОЕ ИЗДЕЛИЕ, БУЛОЧКА ПШЕНИЧНАЯ.'
string_for_parse_1 = "ПН/СР/ПТ/ВС: НАРЕЗКА МЯСНАЯ, ОМЛЕТ НАТУРАЛЬНЫЙ. ВТ/ЧТ/СБ: НАРЕЗКА СЫРНАЯ, КАША РИСОВАЯ МОЛОЧНАЯ С КУРАГОЙ"
string_for_parse_2 = "ПН/СР/ПТ/ВС: САЛАТ ИЗ Б/К КАПУСТЫ С ЗЕЛЕНЬЮ, СУП-ЛАПША КУРИНАЯ, СВИНИНА ТУШЕНАЯ С ОВОЩАМИ, РИС ОТВАРНОЙ, КОНДИТЕРСКОЕ ИЗДЕЛИЕ. ВТ/ЧТ/СБ: САЛАТ ИЗ СВЕЖИХ ОВОЩЕЙ, ЩИ ИЗ Б/К КАПУСТЫ С КУРИЦЕЙ И СМЕТАНОЙ, КУРИНОЕ ФИЛЕ ТУШЕНОЙ, МАКАРОНЫ ОТВАРНЫЕ КОНДИТЕРСКОЕ  ИЗДЕЛИЕ"
string_for_parse_3 = "1 РАЦИОН (ПН, СР, ПТ, ВСК.): САЛАТ ИЗ Б/К КАПУСТЫ, ОГУРЦОВ И КУКУРУЗЫ КОНСЕРВИРОВАННОЙ, СУП КАРТОФЕЛЬНЫЙ С РИСОМ И КУРИЦЕЙ, ГУЛЯШ ИЗ ГОВЯДИНЫ С КАРТОФЕЛЕМ ОТВАРНЫМ, СОК, КОНДИТЕРСКОЕ ИЗДЕЛИЕ, БУЛОЧКА ПШЕНИЧНАЯ. 2 РАЦИОН (ВТ, ЧТ., СУБ.): ОВОЩИ НАТУРАЛЬНЫЕ (ОГУРЦЫ, ПОМИДОРЫ), БОРЩ ИЗ СВЕЖЕЙ КАПУСТЫ С КУРИЦЕЙ И СМЕТАНОЙ, КУРИНОЕ ФИЛЕ НЕЖНОЕ, РИС ОТВАРНОЙ, СОК, КОНДИТЕРСКОЕ ИЗДЕЛИЕ, БУЛОЧКА ПШЕНИЧНАЯ"


def get_meal_menu_list(description: str):
    meals_dict = {}
    dishes = []
    days = ()
    description = description.replace(
        ',', ';').replace('.)', ')').replace('.;', ';').replace('.:', ':').replace('. ', ':')
    # description = description.replace('.)', ')')
    # description = description.replace('.;', ';')
    # description = description.replace('.:', ':')
    # description = description.replace('. ', ':')
    meals_list = description.split(':')
    for num, something in enumerate(meals_list, 1):
        if num % 2 != 0:
            days_list = []
            something = something.replace('/', ';')
            days = something.split(';')
            for day in days:
                if '(' in day:
                    index = day.find('(')
                    day = day[index + 1:]
                days_list.append(day.strip(') : ; , .'))
            days = [MEAL_DAYS_MAPPING.get(day) for day in days_list]
            days = tuple(days)
        else:
            founded_string = re.findall(r'\(.*;.*\)', something)
            for string in founded_string:
                string = string.replace(';', ',')
                something = re.sub(r'\(.*;.*\)', string, something, 1)
            pattern = r';\s.{1,10}ОВ\s|;\s{1}.{1,10}ЕМ\s{1}|;\sС\s|;\s.{1,9}МИ\s|;\s.{1,10}ЫМ\s|;\s.{4}ОК\s'
            founded_string = re.findall(pattern, something)
            for string in founded_string:
                if all(dish not in string for dish in EXCLUDED_DISHES):
                    string = string.replace(';', ',')
                    something = re.sub(pattern, string, something, 1)
            something_split = something.split(';')
            for some in something_split:
                dishes.append(some.strip('. , ; :').capitalize())
            meals_dict[days] = dishes
            dishes = []
    var = meals_dict
    return var


if __name__ == "__main__":
    print(get_meal_menu_list(string_for_parse))
    print(get_meal_menu_list(string_for_parse_1))
    print(get_meal_menu_list(string_for_parse_2))
    print(get_meal_menu_list(string_for_parse_3))
