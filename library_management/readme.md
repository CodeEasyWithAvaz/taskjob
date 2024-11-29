# Система управления библиотекой

Эта программа представляет собой систему управления библиотекой, которая позволяет пользователю добавлять, удалять, искать, просматривать и обновлять статус книг в библиотеке.

## Возможности программы

1. **Добавить новую книгу**: Пользователь может добавить новую книгу в библиотеку, введя название книги, автора и год выпуска.
2. **Удалить книгу**: Пользователь может удалить книгу из библиотеки, введя ее ID.
3. **Поиск книги**: Пользователь может искать книги по названию, автору, году выпуска или статусу.
4. **Просмотр всех книг**: Отображаются все книги в библиотеке и их информация.
5. **Обновить статус книги**: Можно изменить статус книги на «доступна» или «выдана».

## Установка и запуск

1. **Скачать с GitHub**:
    None 

2. **Установить Python версии 3.7 или выше**:
   - Программа работает с Python 3.x. Убедитесь, что у вас установлен Python.
   
   Для установки Python: https://www.python.org/downloads/

3. **Файлы библиотеки**:
   - Файл `library.py` содержит функции для управления библиотекой.
   - Файл `main.py` обеспечивает взаимодействие с пользователем и выполняет основную логику программы.

4. **Запуск программы**:
   - Программа запускается через файл `main.py`. Введите следующую команду в терминале:
     ```bash
     python main.py
     ```
   - Для использования программы в терминале можно выбрать различные опции.

## Использование

### 1. Добавить новую книгу
- Вы можете добавить новую книгу в библиотеку, введя название книги, автора и год выпуска.

### 2. Удалить книгу
- Вы можете удалить книгу из библиотеки, введя её ID.

### 3. Поиск книги
- Вы можете искать книги по названию, автору, году выпуска или статусу.

### 4. Просмотр всех книг
- Отобразятся все книги в библиотеке и их информация.

### 5. Обновить статус книги
- Вы можете изменить статус книги на «доступна» или «выдана».

## Структура кода

- **Класс `Book`**: Содержит атрибуты для каждой книги (ID, название, автор, год и статус).
- **Класс `Library`**: Содержит все необходимые методы для управления книгами в библиотеке: добавление, удаление, поиск, обновление статуса и вывод списка книг.


# create by avazbek CodeWithAvaz