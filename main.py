from reader import Reader
from book import Book
from loan import Loan


class Library:
    """Класс Библиотека"""

    def __init__(self, name):
        self.name = name
        self.readers = []
        self.books = []
        self.loans = []
        self.next_loan_id = 1
        self.next_reader_id = 1

    def add_reader(self, full_name, phone):
        """Добавить читателя"""
        reader = Reader(full_name, self.next_reader_id, phone)
        self.readers.append(reader)
        self.next_reader_id += 1
        return reader

    def add_book(self, title, author, year, isbn):
        """Добавить книгу"""
        book = Book(title, author, year, isbn)
        self.books.append(book)
        return book

    def issue_book(self, reader, book, issue_date, due_date):
        """Выдать книгу читателю"""
        if not book.available:
            print(f"⚠️ Книга '{book.title}' уже выдана!")
            return None

        loan = Loan(self.next_loan_id, reader, book, issue_date, due_date)
        self.loans.append(loan)
        book.available = False
        reader.books_taken += 1
        self.next_loan_id += 1
        return loan

    def return_book(self, loan, return_date):
        """Принять возвращённую книгу"""
        loan.return_book(return_date)

    def list_active_loans(self):
        """Показать все активные выдачи"""
        active_loans = [loan for loan in self.loans if loan.status == "Выдана"]

        if not active_loans:
            print("\n⚠️ Нет активных выдач")
            return

        print(f"\n{'=' * 70}")
        print(f"Активные выдачи библиотеки «{self.name}»")
        print(f"{'=' * 70}")
        for loan in active_loans:
            print(loan)
            print("-" * 70)

    def list_all_books(self):
        """Показать все книги"""
        print(f"\n{'=' * 70}")
        print(f"Фонд библиотеки «{self.name}»")
        print(f"{'=' * 70}")
        for book in self.books:
            print(book)
        print(f"{'=' * 70}")
        print(f"Всего книг: {len(self.books)}")


# === ДЕМОНСТРАЦИЯ РАБОТЫ ===
if __name__ == "__main__":
    # Создаём библиотеку
    library = Library("Научная библиотека КубГТУ")

    # Добавляем читателей
    print("Регистрируем читателей...")
    reader1 = library.add_reader("Иванов Иван Иванович", "+7 (918) 123-45-67")
    reader2 = library.add_reader("Петрова Мария Сергеевна", "+7 (918) 987-65-43")
    reader3 = library.add_reader("Сидоров Пётр Алексеевич", "+7 (918) 456-78-90")
    print(f"✅ {reader1}")
    print(f"✅ {reader2}")
    print(f"✅ {reader3}")

    # Добавляем книги
    print("\nДобавляем книги в фонд...")
    book1 = library.add_book("Программирование на Python", "Лутц Марк", 2020, "978-5-91180-123-4")
    book2 = library.add_book("Алгоритмы. Построение и анализ", "Кормен Томас", 2019, "978-5-8459-1234-5")
    book3 = library.add_book("Чистый код", "Мартин Роберт", 2021, "978-5-4461-2345-6")
    book4 = library.add_book("Паттерны проектирования", "Ганг оф Фор", 2018, "978-5-91180-345-7")
    print(f"✅ {book1}")
    print(f"✅ {book2}")
    print(f"✅ {book3}")
    print(f"✅ {book4}")

    # Выдаём книги
    print("\nВыдаём книги читателям...")
    loan1 = library.issue_book(reader1, book1, "15.02.2026", "01.03.2026")
    loan2 = library.issue_book(reader2, book2, "16.02.2026", "02.03.2026")
    loan3 = library.issue_book(reader1, book3, "17.02.2026", "03.03.2026")
    print(f"✅ Выдана: {book1.title} → {reader1.full_name}")
    print(f"✅ Выдана: {book2.title} → {reader2.full_name}")
    print(f"✅ Выдана: {book3.title} → {reader1.full_name}")

    # Возвращаем книгу
    print("\n📥 Читатель возвращает книгу...")
    library.return_book(loan1, "25.02.2026")
    print(f"✅ Книга '{book1.title}' возвращена {reader1.full_name}")

    # Показываем все книги
    library.list_all_books()

    # Показываем активные выдачи
    library.list_active_loans()

    print(f"\n{'=' * 70}")
    print("Информационная система библиотеки успешно завершила работу")
    print(f"{'=' * 70}")