from utlis import books

def add_book():
    book_name = input("Enter a book name:").strip().upper()
    books.append(book_name)
    print(f"Book- {book_name} added successfully.")


