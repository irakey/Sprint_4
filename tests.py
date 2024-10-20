from main import BooksCollector

import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_init_books_collector(self, books_collector):
        assert books_collector.books_genre == {}

        assert books_collector.favorites == []

        expected_genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books_collector.genre == expected_genres

        expected_genre_age_rating = ['Ужасы', 'Детективы']
        assert books_collector.genre_age_rating == expected_genre_age_rating

    @pytest.mark.parametrize("book_name, genre", [
        ('Звездные войны', 'Фантастика'),
        ('Детские сказки', 'Мультфильмы'),
        ('Война и мир', 'Ужасы')
    ])
    def test_set_book_genre_valid(self, books_collector, book_name, genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    def test_get_book_genre_not_exist_book(self, books_collector):
        assert books_collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_existing_books(self, books_collector):
        books_collector.add_new_book('Война и мир')
        books_collector.set_book_genre('Война и мир', 'Фантастика')

        books_collector.add_new_book('Незнайка')
        books_collector.set_book_genre('Незнайка', 'Мультфильмы')

        books_collector.add_new_book('Король Лев')
        books_collector.set_book_genre('Король Лев', 'Мультфильмы')

        assert books_collector.get_books_with_specific_genre('Мультфильмы') == ['Незнайка', 'Король Лев']

    @pytest.mark.parametrize("book_name, genre", [
        ('Автобиография', 'Комедии'),
        ('Сказки для детей', 'Мультфильмы'),
    ])
    def test_get_book_genre_valid(self, books_collector, book_name, genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book('Детские сказки')
        books_collector.set_book_genre('Детские сказки', 'Фантастика')

        books_collector.add_new_book('Поворот не туда')
        books_collector.set_book_genre('Поворот не туда', 'Ужасы')

        books_collector.add_new_book('Холмс')
        books_collector.set_book_genre('Холмс', 'Детективы')

        books_collector.add_new_book('Сказки для детей')
        books_collector.set_book_genre('Сказки для детей', 'Мультфильмы')

        expected_books = ['Детские сказки', 'Сказки для детей']

        assert books_collector.get_books_for_children() == expected_books

    def test_add_book_in_favorites_valid(self, books_collector):
        books_collector.add_new_book('Русалочка')
        books_collector.set_book_genre('Русалочка', 'Фантастика')
        books_collector.add_book_in_favorites('Русалочка')

        assert 'Русалочка' in books_collector.favorites

    def test_delete_book_from_favorites_valid(self, books_collector):
        books_collector.add_new_book('Русалочка')
        books_collector.set_book_genre('Русалочка', 'Фантастика')
        books_collector.add_book_in_favorites('Русалочка')
        books_collector.delete_book_from_favorites('Русалочка')

        assert 'Русалочка' not in books_collector.favorites

    def test_get_list_of_favorites_books_valid(self, books_collector):
        books_collector.add_new_book('Русалочка')
        books_collector.set_book_genre('Русалочка', 'Фантастика')
        books_collector.add_book_in_favorites('Русалочка')

        assert books_collector.get_list_of_favorites_books() == ['Русалочка']



