class Book:
   # Constructor
   def __init__(self, title, author):
     self.title = title
     self.author = author
     self.is_borrowed = False

# Borrow a book
def borrow(self):
    if not self.is_borrowed:
        self.is_borrowed = True
    else:
        print(self.title, "is already borrowed")

# Return a book
def returned(self):
    if not self.is_returned:
        self.is_returned = False
    else:
        print(self.title, "is not returned") 

# Create book objects
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Diary of a wimpy kid", "Jeff Kinney")

# Display books

print(book1)

print(book2)

print(book3)

# Demonstrate borrowing and returning
book1.borrow()
book1.borrow()
book1.return_book()

# Display updated information
print(book1)