from page_object.helpers import generate_phone_number

ORDER_INFO_DICT = {
    'metro': 'октябрьская',
    'colour': 'серый',
    'phone': generate_phone_number(),
    'address': 'test street, 7'
}


class AnswerText:

    ANSWER_TEXT_PRICE = 'Стоимость - 400 рублей в сутки.'
    ANSWER_TEXT_1 = 'Какой-то еще ответ на вопрос.'

