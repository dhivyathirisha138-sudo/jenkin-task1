class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to library.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index].borrow_book()
        else:
            print("Invalid book index.")

    def return_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index].return_book()
        else:
            print("Invalid book index.")


def main():
    library = Library()

    # Sample books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    while True:
        print("\n--- Library Menu ---")
        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            library.show_books()
        elif choice == "2":
            library.show_books()
            index = int(input("Enter book number to borrow: ")) - 1
            library.borrow_book(index)
        elif choice == "3":
            library.show_books()
            index = int(input("Enter book number to return: ")) - 1
            library.return_book(index)
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
