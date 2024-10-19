Список тестов:
1. `test_add_new_book_add_two_books` Проверяется метод add_new_book для двух книг.
2. `test_set_book_genre_add_genre_is_list_genre_and_add_genre_is_not_list_genre` Проверяется метод set_book_genre для жанра из списка gerne и для жанра не из спика genre. Также проверяется метод get_books_genre. Тест параметризирован.
3. `test_get_book_genre_get_genre_is_fantastic` Проверяется метод get_book_genre для жанра Фантастика. 
4. `test_get_books_with_specific_genre_get_one_books_of_the_fantastic` Проверяется метод get_books_with_specific_genre. Добавляем две книги разных жанров. В результате получаем наименование одной книги по запрашиваемому жанру.
5. `test_get_books_genre_get_three_books` Проверяется метод get_books_genre. Ожидаем получить словарь из трех элементов.
6. `test_get_books_for_children_get_one_book_is_fantastic` Проверяется метод get_books_for_children. Тест параметризован. Тестовые данные подготовлены для каждого жанра из списка genre.
7. `test_add_book_in_favorites_add_two_books` Проверяется метод add_book_in_favorites. Из трех книг две добавляем в список favorites и проверяем длину списка.
8. `test_delete_book_from_favorites_delete_one_book` Проверяется метод delete_book_from_favorites. Из трех книг две добавляем в список favorites, одну удаляем и проверяем длину списка.
9. `test_get_list_of_favorites_books_two_books_in_list_favorites` Проверяется метод get_list_of_favorites_books. Из трех книг две добавляем в список и ожидаем увидеть список из двух элементов.