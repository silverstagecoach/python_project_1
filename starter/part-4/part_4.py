### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

def create_new_book():
    title = input("What is your title of this book? - ")
    author = input("Who is the author of this book? - ")
    year = input("What year was this book written? - ")
    rating = input("What is the rating you would give this book? - ")
    pages = input("How many pages does this book have? - ")

    book_dictionary = {
        "title":title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def create_newer_book():
    title = str(input("What is your title of this book? - "))
    author = str(input("Who is the author of this book? - "))
    year = int(input("What year was this book written? - "))
    rating = float(input("What is the rating you would give this book? - "))
    pages = int(input("How many pages does this book have? - "))

    book_dictionary = {
        "title":title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_newest_book():
    title = input("What is your title of this book? - ")
    author = input("Who is the author of this book? - ")
    try:
        year = input("What year was this book written? - ")
    except:
        year = int(input("Please type a number for the year. - "))
    try:
        rating = float(input("What is the rating you would give this book? - "))
    except:
        rating = float(input("Please type a number for the rating. -"))
    try:
        pages = int(input("How many pages does this book have? - "))
    except:
        pages = int(input("Please type a number for the pages. - "))


    book_dictionary = {
        "title":title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
if select_book:
    for book in book_library:

elif select_author:
    for author in book_library:

else exit_library:


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

while 