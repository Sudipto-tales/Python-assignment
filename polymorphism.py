#Library Management System

class Library:
    def take(self):
        pass

class Book(Library):
    def __init__(self, book_name, book_author):
        self.name = book_name
        self.author = book_author

    def take(self):
        book_name = input("Book Name: ")
        book_author = input("Book Author: ")
        print(f"\nYou borrowed the book: {book_name} written by {book_author} from Library.")
        return book_name, book_author

class Magazine(Library):
    def __init__(self, manga_name, manga_author):
        self.name = manga_name
        self.author = manga_author

    def take(self):
        manga_name = input("Magazine Name: ")
        manga_author = input("Magazine Author: ")
        print(f"You borrowed the magazine: {manga_name} by {manga_author}")
        return manga_name, manga_author

class User(Library):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def take(self):
        name = input("Your Name: ")
        age = input("Age: ")
        print(f"Welcome, {name}!")
        return name, age

if __name__ == "__main__":
    user = User("", 0)
    user.take()

    print("Choose What you need:")
    print("1. Book")
    print("2. Magazine")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = Book("", "")
        book.take()
    elif choice == 2:
        magazine = Magazine("", "")
        magazine.take()
    else:
        print("Invalid choice!")
