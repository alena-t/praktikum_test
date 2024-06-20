import pytest


class TestBooks:

    @pytest.mark.parametrize(
        'score, expected_result',
        [
            [7, 1], [5, 2], [3, 3]
        ]
    )
    def test_get_book_success(self, book, score, expected_result):
        result = book.get_book(score)
        assert len(result) == expected_result

    def test_get_book_failed(self, book):
        assert book.get_book() == result
