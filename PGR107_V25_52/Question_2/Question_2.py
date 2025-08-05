#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 12 10:08:56 2025

@author: Candidate 52
"""

# SOURCES

#   * Title    : How to use the if not in Python statement?
#   * Author   : Ancil Eric D'Silva
#   * Date     : n.d
#   * Accessed : 2025-05-12
#   * URL      : https://flexiple.com/python/if-not-python

#   * Title    : __init__ in Python
#   * Author   : GeeksForGeeks.org
#   * Date     : 2024-12-13
#   * Accessed : 2025-05-12
#   * URL      : https://www.geeksforgeeks.org/__init__-in-python/

import Question_2_Book_Module as book_module
import Question_2_Library_Module as library_module
    
def main():
    library_instance = library_module.Library()
    
    while(True):
        print("\n-------------- Menu options --------------")
        print("> (1): Add a new book to the library.")
        print("> (2): Remove a book from the library.")
        print("> (3): Check out a book from the library.")
        print("> (4): Check in a book to the library.")
        print("> (5): See all books in the library.")
        print("> (6): Leave the library.")
        menu_choice = input("Choice: ")
        
        if(menu_choice == "1"):
            title = input("\n> Enter title of the book: ")
            author = input("> Enter the author of the book: ")
            while True:
                try:
                    num_pages = int(input("> Enter number of pages in the book: "))
                    break
                except ValueError:
                    print("\n - Invalid input, please enter a number for the number of pages.")
            borrowed = False
            book_instance = book_module.Book(title, author, num_pages, borrowed)
            library_instance.add_book(book_instance)
            print(f"\n - The book '{book_instance.title}' was added to the library")
            
        elif(menu_choice == "2"):
            title = input("\n> Enter title of the book you wish to remove: ")
            library_instance.remove_book(title)
            
        elif(menu_choice == "3"):
            title = input("\n> Enter title of the book you wish to check out: ")
            library_instance.check_out(title)
            
        elif(menu_choice == "4"):
            title = input("\n> Enter title of the book you wish to check in: ")
            library_instance.check_in(title)
            
        elif(menu_choice == "5"):
            print("\nAll books in the libray: \n")
            if not library_instance.books:
                print(" - There are no books in the library, please add some.")
            else:
                library_instance.show_all_books()
            
        elif(menu_choice == "6"):
            print("\n - Exiting the library.")
            break
        else:
            print("\n - This is not a valid menu choice, please try again.")
            
if __name__ == "__main__":
    main()