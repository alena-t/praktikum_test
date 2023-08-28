# подготовленные данные
books = [
    {
        'name': 'Алиса в стране чудес.',
        'frequency_of_use': 2,
        'year_of_writing': 1865,
        'genre': ['fairy_tale', 'absurd']
    },
    {
        'name': 'Хоббит, или Туда и обратно.',
        'frequency_of_use': 3,
        'year_of_writing': 1937,
        'genre': ['fairy_tale', 'fantasy']
    },
    {
        'name': 'Гарри Поттер и Кубок огня',
        'frequency_of_use': 2.5,
        'year_of_writing': 2000,
        'genre': ['fantasy', 'adventure']
    }
]

movies = ['Гарри Поттер и Кубок огня', 'Властелин колец', 'Алиса в стране чудес.']


# опиши тут стаб, который поможет написать тест без засисимости
class DataBaseClient:

    def __init__(self, data):
        self.data = data
        self.movies = None

    def get_all_books(self):
        return self.data

    def set_movies_list(self, movies):
        self.movies = movies
        return movies

    def get_movies_by_books(self):
        movies_by_books = []
        for book in self.data:
            if book.get('name') in self.movies:
                movies_by_books.append(book.get('name'))
        return movies_by_books


# тестируемая функция
def get_movies_based_on_books(books, movies):
    client = DataBaseClient(books)
    client.set_movies_list(movies)
    movies = client.get_movies_by_books()
    return movies


if __name__ == '__main__':
    print(get_movies_based_on_books(books, movies))
