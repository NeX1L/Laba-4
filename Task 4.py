class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Книга: {self.title}, Автор: {self.author}, Год издания: {self.year}"

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def get_genre(cls):
        return "Роман"


book1 = Book("Война и мир", "Лев Толстой", 1869)
print(book1.display_info())
year = 2000
print(f"Год {year} {'високосный' if Book.is_leap_year(year) else 'не високосный'}")

print(f"Жанр книги: {Book.get_genre()}")
