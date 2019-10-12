class Library:

    def __init__(self, listOfBooks, authorName):
        self.listOfBooks = listOfBooks
        self.authorName = authorName
        self.lend_books = {}

        for book in self.listOfBooks:
            self.lend_books[book] = None

    def displayBooks(self):
        for index, book in enumerate(self.listOfBooks):
            print(str(index + 1) + ": " + book + "")

    def addBooks(self, bookName):
        self.listOfBooks.append(bookName)
        self.lend_books[bookName] = None

    def lendBooks(self, bookName, authorName):
        print('zbc')
        if bookName in self.listOfBooks:
            print("Congrats")
            if self.lend_books[bookName] is None:
                self.lend_books[bookName] = authorName
            else:
                print("This book is alreay lend by" + self.lend_books[bookName])
        else:
            print("This book is not present in the library!")

    def returnBook(self, bookName):
        if bookName in self.listOfBooks:
            if self.lend_books is not None:
                self.lend_books.pop(bookName)
                self.lend_books[bookName]=None
            else:
                print("This book is not lended by someone")
        else:
            print("This book doesnot belongs to this library")

    def deleteBook(self, bookName):
        self.listOfBooks.remove(bookName)
        self.lend_books.pop(bookName)


def main():
    listOfBooks = ['Passenger', 'Harry Potter', 'Paul Coelho', 'Kolkata', 'Vibha']
    LibraryName = 'Roshan'

    r = Library(listOfBooks, LibraryName)

    print(
        f"****Welcome to {LibraryName} Library****\n\nPlease select the following options:\n\t0. Exit\n\t1. Diplay Books\n\t2. Add Books\n\t3. Lend\n\t4. Return\n\t5. Delete")

    while True:
        choice = input("Enter your choice :\n")

        if choice == 0:
            exit()

        elif choice == '1':
            r.displayBooks()

        elif choice == '2':
            bookName = input("Please enter the book name :\n")
            r.addBooks(bookName)

        elif choice == '3':
            bName = input("Enter the book name : ")
            owner = input("Enter the person name : ")
            r.lendBooks(bName, owner)

        elif choice == '4':
            bookName = input("Enter the book name : ")
            r.returnBook(bookName)

        elif choice == '5':
            bookName = input("Enter the book name to delete : ")
            r.deleteBook(bookName)


if __name__ == "__main__":
    main()
