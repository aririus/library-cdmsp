class Book:
    """Класс Книга"""

    def __init__(self, title, author, year, isbn, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "доступна" if self.available else "выдана"
        return f"📚 '{self.title}' | {self.author} ({self.year}) | ISBN: {self.isbn} | Статус: {status}"