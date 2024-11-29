import json
from typing import List, Dict, Union

STORAGE_FILE = "./storage.json"

class Book:
    """Объект книги"""
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "доступен"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self) -> str:
        return f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"

class Library:
    """Система управления библиотекой"""

    def __init__(self):
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """Загрузка книг из библиотеки."""
        try:
            with open(STORAGE_FILE, "r") as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self) -> None:
        """Сохранение книг в файл."""
        with open(STORAGE_FILE, "w") as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавить новую книгу."""
        new_id = len(self.books) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга успешно добавлена: {new_book}")

    def delete_book(self, book_id: int) -> None:
        """Удалить книгу."""
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def search_books(self, key: str, value: Union[str, int]) -> None:
        """Поиск книги."""
        valid_keys = ["title", "author", "year", "status"]
        if key not in valid_keys:
            print(f"Ошибка: Неверный ключ поиска. Выберите один из следующих ключей: {', '.join(valid_keys)}.")
            return
        results = [book for book in self.books if str(getattr(book, key)).lower() == str(value).lower()]
        if results:
            print("Результаты поиска:")
            for book in results:
                print(book)
        else:
            print("Не найдено никаких результатов.")

    def list_books(self) -> None:
        """Показать все книги."""
        if self.books:
            print("Книги в библиотеке:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")

    def update_status(self, book_id: int, status: str) -> None:
        """Обновить статус книги."""
        if status not in ["доступен", "выдан"]:
            print("Ошибка: Статус должен быть 'доступен' или 'выдан'.")
            return
        for book in self.books:
            if book.book_id == book_id:
                book.status = status
                self.save_books()
                print(f"Статус книги обновлен (ID: {book_id}, Новый статус: {status}).")
                return
        print("Книга с таким ID не найдена.")


# create by avazbek CodeWithAvaz