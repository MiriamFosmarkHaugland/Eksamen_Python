#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 12:30:31 2025

@author: Candidate 52
"""

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, title):
        found_book = False
        if not self.books:
            print(" - There are no books in the library, please add some first.")
            return
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                found_book = True
                print(f" - The book '{title}' was removed from the library.")
                return
        if not found_book:
            print(f" - Found no book with the title: '{title}', please try again.")
            
    def check_out(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrowed:
                    print(f" - The book '{title}' is already checked out, wait for the book to be checked in or find another one.")
                else:
                    book.borrowed = True
                    print(f" - The book '{title}' is now checked out.")
                return
        print(f" - Found no book with the title: '{title}', please try again.")
                
    def check_in(self, title):
        for book in self.books:
            if book.title == title:
                if not book.borrowed:    
                    print(f" - The book '{title}' is not checked out, check out the book first before you can check it in.")
                else:
                    book.borrowed = False
                    print(f" - The book '{title}' is now checked in.")
                return
        print(f" - Found no book with the title: '{title}', please try again.")
        
    def show_all_books(self):
        for book in self.books:
            all_books = str(book)
            print(all_books)