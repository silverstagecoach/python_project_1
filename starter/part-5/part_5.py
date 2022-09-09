### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
with open("library.txt", "a") as f:
    f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
with open("library.txt", "r") as f:
    file = f.readlines()

    for line in file:
        line = line.split(", ")

        book_dictionary = {
            "title": line[0],
            "author": line[1],
            "year": line[2],
            "rating": line[3],
            "pages": line[4]
        }


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

if __name__ == '__main__':
    main_menu()
