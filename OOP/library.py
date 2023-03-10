class Library:
    def displayAvailableBooks(self):
        pass

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")
    def addBook(self):
        pass


class Customer:
    def requestBook(self):
        print("Enter the name of  book you would like to borrow:")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book

library = Library('Think and Grow Ritch', "Who Will Cry When You Die", "For One More Day")
customer =  Customer()
print("Enter 1 to display the available bo")
