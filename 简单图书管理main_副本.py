class Book:
    def __init__(self, title, author, publish_date, ISBN):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.ISBN = ISBN

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def update_book(self, title, new_book):
        for i, book in enumerate(self.books):
            if book.title == title:
                self.books[i] = new_book
                return True
        return False

    def list_books(self):
        for book in self.books:
            print("book title：", book.title)
            print("author：", book.author)
            print("Publication Date：", book.publish_date)
            print("ISBN：", book.ISBN)
            print("------------------")

def main():
    library = Library()
    while True:
        print("1. Add books")
        print("2. Search for books")
        print("3. Delete Book")
        print("4. Update book information")
        print("5. List all books")
        print("6. exit")
        choice = input("Please enter your selection：")
        if choice == '1':
            title = input("Please enter the book title：")
            author = input("Please enter the author：")
            publish_date = input("Please enter the publication date：")
            ISBN = input("Please tnter ISBN：")
            book = Book(title, author, publish_date, ISBN)
            library.add_book(book)
            print("Book added successfully！")
        elif choice == '2':
            title = input("Please enter the title of the book you are looking for：")
            book = library.find_book(title)
            if book:
                print("Find Books！")
                print("book title：", book.title)
                print("author：", book.author)
                print("Publication Date：", book.publish_date)
                print("ISBN：", book.ISBN)
            else:
                print("Sorry, I couldn't find this book。")
        elif choice == '3':
            title = input("Please enter the title of the book you want to delete：")
            if library.delete_book(title):
                print("Book deleted successfully！")
            else:
                print("Sorry, I couldn't find this book。")
        elif choice == '4':
            title = input("Please enter the book title you want to update：")
            new_title = input("Please enter a new book title：")
            new_author = input("Please enter a new author：")
            new_publish_date = input("Please enter a new publication date：")
            new_ISBN = input("Please enter a new ISBN：")
            new_book = Book(new_title, new_author, new_publish_date, new_ISBN)
            if library.update_book(title, new_book):
                print("Book information updated successfully！")
            else:
                print("Sorry, I couldn't find this book。")
        elif choice == '5':
            library.list_books()
        elif choice == '6':
            break
        else:
            print("Invalid selection, please re-enter。")

if __name__ == "__main__":
    main()
