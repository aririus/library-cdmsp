class Reader:
    """Класс Читатель"""

    def __init__(self, full_name, reader_id, phone):
        self.full_name = full_name
        self.reader_id = reader_id
        self.phone = phone
        self.books_taken = 0

    def __str__(self):
        return f"📖 Читатель: {self.full_name} | ID: {self.reader_id} | Тел: {self.phone} | Книг на руках: {self.books_taken}"