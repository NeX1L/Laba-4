class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f"Книга: {self.title}, Автор: {self.author}, Год издания: {self.year}"

    @staticmethod
    def visikosny(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def janr(cls):
        return "Роман"

if __name__ == '__main__':
    book1 = Book("Война и мир", "Лев Толстой", 1869)
    print(book1.display())
    year = 2000
    print(f"Год {year} {'високосный' if Book.visikosny(year) else 'не високосный'}")

    print(f"Жанр книги: {Book.janr()}")
