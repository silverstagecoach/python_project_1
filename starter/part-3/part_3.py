from ast import If


my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_title_parser(book_dictionary):
    book_title = book_dictionary["title"]
    book_string = f"This is the title of your book: {book_title}"
    return book_string

print(book_title_parser(my_book))
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_author_parser(book_dictionary):
    book_author = book_dictionary["author"]
    book_string = f"This is the author of your book: {book_author}"
    return book_string

print(book_author_parser(my_book))
    
def book_year_parser(book_dictionary):
    book_year = book_dictionary["year"]
    book_string = f"This is the year of publication for your book: {book_year}"
    return book_string

print(book_year_parser(my_book))

def book_rating_parser(book_dictionary):
    book_rating = book_dictionary["rating"]
    book_string = f"This is the rating of your book: {book_rating}"
    return book_string

print(book_rating_parser(my_book))

def book_pages_parser(book_dictionary):
    book_pages = book_dictionary["pages"]
    book_string = f"This is the number of pages in your book: {book_pages}"
    return book_string

print(book_pages_parser(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def find_book(string):
    if string == my_book[0]:
        return f"Your request for {string} was found."
    else:
        return "Your request could not be found."

def print_out_books():
    for book in all_books_list:
        print(book)

def correct_info(arguement_string, correction_string):
    for element in my_book:
        if arguement_string == element:
            element = correction_string