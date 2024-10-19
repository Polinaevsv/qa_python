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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book_name, genre, expected', [['Потерянные девушки Рима', 'Детективы', {'Потерянные девушки Рима': 'Детективы'}], ['Темное полнолуние', 'Фэнтези', {'Темное полнолуние': ''}]])
    def test_set_book_genre_add_genre_is_list_genre_and_add_genre_is_not_list_genre(self, collector, book_name, genre, expected):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_books_genre() == expected


    def test_get_book_genre_get_genre_is_fantastic(self, collector):
        collector.add_new_book('Гарри Поттер и филосовский камень')
        collector.set_book_genre('Гарри Поттер и филосовский камень', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер и филосовский камень') == 'Фантастика'

    def test_get_books_with_specific_genre_get_one_books_of_the_fantastic(self, collector):

        collector.add_new_book('Гарри Поттер и тайная комната')
        collector.add_new_book('Охотник за тенью')
        collector.set_book_genre('Гарри Поттер и тайная комната', 'Фантастика')
        collector.set_book_genre('Охотник за тенью', 'Детективы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер и тайная комната']


    def test_get_books_genre_get_three_books(self, collector):
        collector.add_new_book('Вокруг света за 80 дней')
        collector.add_new_book('Дом с душой ведьм')
        collector.add_new_book('Охотник за тенью')
        collector.set_book_genre('Вокруг света за 80 дней', 'Фантастика')
        collector.set_book_genre('Дом с душой ведьм', 'Ужасы')
        collector.set_book_genre('Охотник за тенью', 'Детективы')

        assert collector.get_books_genre() == {'Вокруг света за 80 дней': 'Фантастика', 'Дом с душой ведьм': 'Ужасы', 'Охотник за тенью': 'Детективы'}

    @pytest.mark.parametrize('book_name, genre, expected', [['Вокруг света за 80 дней', 'Фантастика', ['Вокруг света за 80 дней']], ['Охотник за тенью', 'Детективы', []], ['Дом с душой ведьм', 'Ужасы', []], ['Винни Пух', 'Мультфильмы', ['Винни Пух']], ['Приключения Миши и Маши', 'Комедии', ['Приключения Миши и Маши']]])
    def test_get_books_for_children_get_one_book_is_fantastic(self, collector, book_name, genre, expected):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_books_for_children() == expected


    def test_add_book_in_favorites_add_two_books(self, collector):
        collector.add_new_book('Вокруг света за 80 дней')
        collector.add_new_book('Дом с душой ведьм')
        collector.add_new_book('Охотник за тенью')

        collector.add_book_in_favorites('Вокруг света за 80 дней')
        collector.add_book_in_favorites('Охотник за тенью')

        assert len(collector.get_list_of_favorites_books()) == 2


    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Вокруг света за 80 дней')
        collector.add_new_book('Дом с душой ведьм')
        collector.add_new_book('Охотник за тенью')

        collector.add_book_in_favorites('Вокруг света за 80 дней')
        collector.add_book_in_favorites('Охотник за тенью')

        collector.delete_book_from_favorites('Охотник за тенью')

        assert len(collector.get_list_of_favorites_books()) == 1


    def test_get_list_of_favorites_books_two_books_in_list_favorites(self, collector):
        collector.add_new_book('Вокруг света за 80 дней')
        collector.add_new_book('Дом с душой ведьм')
        collector.add_new_book('Охотник за тенью')

        collector.add_book_in_favorites('Вокруг света за 80 дней')
        collector.add_book_in_favorites('Охотник за тенью')

        assert collector.get_list_of_favorites_books() == ['Вокруг света за 80 дней', 'Охотник за тенью']

