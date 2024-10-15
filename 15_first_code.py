
class TestClass:

    @pytest.mark.parametrize(
        'name, books_count',
        [
            (['Гордость и предубеждение'], 1),
            (['Гордость и предубеждение', 'Гарри Поттер и ...'], 2),
            ([], 0)
        ]
    )
    def test_add_book_to_favorite(self, book, name, books_count):
        for book_name in name:
            book.add_book_to_favorite(book_name)
        favorite = book.get_favorite_books()
        assert len(favorite) == books_count
