from datetime import datetime


class Loan:
    """Класс Выдача книги читателю"""

    def __init__(self, loan_id, reader, book, issue_date, due_date):
        self.loan_id = loan_id
        self.reader = reader
        self.book = book
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = None
        self.status = "Выдана"

    def return_book(self, return_date):
        """Вернуть книгу"""
        self.return_date = return_date
        self.status = "Возвращена"
        self.book.available = True
        self.reader.books_taken -= 1

    def __str__(self):
        result = f"📋 Запись №{self.loan_id}\n"
        result += f"   Читатель: {self.reader.full_name} (ID: {self.reader.reader_id})\n"
        result += f"   Книга: '{self.book.title}' ({self.book.author})\n"
        result += f"   Выдана: {self.issue_date}\n"
        result += f"   Должна быть возвращена: {self.due_date}\n"
        if self.return_date:
            result += f"   Возвращена: {self.return_date}\n"
        result += f"   Статус: {self.status}"
        return result