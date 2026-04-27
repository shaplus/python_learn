class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")
    
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book removed: {book.title}")
                return
        print(f"Book with ISBN {isbn} not found")
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def borrow_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            if book.available:
                book.available = False
                print(f"Book borrowed: {book.title}")
            else:
                print(f"Book {book.title} is already borrowed")
        else:
            print(f"Book with ISBN {isbn} not found")
    
    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            if not book.available:
                book.available = True
                print(f"Book returned: {book.title}")
            else:
                print(f"Book {book.title} is already available")
        else:
            print(f"Book with ISBN {isbn} not found")
    
    def list_books(self):
        if not self.books:
            print("No books in the library")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

# 使用示例
library = Library()

# 添加书籍
book1 = Book("Python Programming", "John Doe", "1234567890")
book2 = Book("Data Science Basics", "Jane Smith", "0987654321")
library.add_book(book1)
library.add_book(book2)

# 列出书籍
library.list_books()

# 借阅书籍
library.borrow_book("1234567890")
library.list_books()

# 归还书籍
library.return_book("1234567890")
library.list_books()

# 移除书籍
library.remove_book("0987654321")
library.list_books()