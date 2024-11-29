import unittest
import os
from unittest.mock import patch
from io import StringIO
from library import Library, Book, STORAGE_FILE

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.library = Library()
        self.library.books = []
        self.library.save_books()

    def tearDown(self):
        """Очистка после каждого теста."""
        if os.path.exists(STORAGE_FILE):
            os.remove(STORAGE_FILE)

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Python Programming")
        self.assertEqual(self.library.books[0].author, "John Doe")
        self.assertEqual(self.library.books[0].year, 2020)

    def test_delete_book(self):
        """Тест удаления книги."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        book_id = self.library.books[0].book_id
        self.library.delete_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books_by_title(self):
        """Тест поиска книг по названию."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.library.search_books("title", "Python Programming")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Python Programming", output)

    def test_search_books_invalid_key(self):
        """Тест с неверным ключом поиска."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.library.search_books("invalid_key", "Python Programming")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Xato", output)

    def test_update_status(self):
        """Тест обновления статуса книги."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        book_id = self.library.books[0].book_id
        self.library.update_status(book_id, "berilgan")
        self.assertEqual(self.library.books[0].status, "berilgan")

    def test_update_status_invalid(self):
        """Тест с неверным обновлением статуса."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        book_id = self.library.books[0].book_id
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.library.update_status(book_id, "not_valid_status")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Xato", output)

    def test_list_books_empty(self):
        """Тест на вывод книг в пустой библиотеке."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.library.list_books()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Kutubxona bo'sh", output)

    def test_list_books(self):
        """Тест на вывод книг, если библиотека не пуста."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.library.list_books()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Python Programming", output)

    def test_load_books(self):
        """Тест на загрузку книг из файла хранилища."""
        self.library.add_book("Python Programming", "John Doe", 2020)
        self.library.save_books()
        new_library = Library()
        new_library.load_books()
        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "Python Programming")

if __name__ == "__main__":
    unittest.main()


# create by avazbek CodeWithAvaz