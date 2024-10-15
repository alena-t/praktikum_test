import pytest

from helpers import generate_book_name


@pytest.fixture
def books_collector():
    return BooksCollector()


class TestBooks:


    @pytest.mark.parametrize(
        'book_name',
        [
            'Гарри Поттер и Узник Азкабана',
            'Хоббит: туда и обратно',
        ]
    )
    def test_add_new_book(self, books_collector, book_name):

        books_collector.add_new_book(name=book_name)

        books_dict = books_collector.get_books()

        assert books_dict.get(book_name)

    def test_add_book_genre(self, books_collector):
        pass

