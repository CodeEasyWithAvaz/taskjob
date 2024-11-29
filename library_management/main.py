from library import Library

def main():
    """Основная программа."""
    library = Library()

    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить новую книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Обновить статус книги")
        print("6. Выход")
        choice = input("Введите ваш выбор (1-6): ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год книги: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: Год должен быть целым числом.")
        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)
            except ValueError:
                print("Ошибка: ID книги должен быть целым числом.")
        elif choice == "3":
            key = input("Введите ключ для поиска (title, author, year, status): ")
            value = input("Введите значение для поиска: ")
            library.search_books(key, value)
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги для обновления статуса: "))
                status = input("Введите новый статус ('доступен' или 'выдан'): ")
                library.update_status(book_id, status)
            except ValueError:
                print("Ошибка: Введите правильный ID книги и статус.")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор.")

if __name__ == "__main__":
    main()


# created by avazbek CodeWithAvaz