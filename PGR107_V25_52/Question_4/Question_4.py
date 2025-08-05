#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 09:37:28 2025

@author: Candidate 52
"""

# SOURCES

#   * Title    : Best way to strip punctuation from a string
#   * Author   : Brian
#   * Date     : 2008-11-05
#   * Accessed : 2025-05-20
#   * URL      : https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string

#   * Title    : Python string strip() Method
#   * Author   : GeeksForGeeks.org
#   * Date     : 2025-05-01
#   * Accessed : 2025-05-20
#   * URL      : https://www.geeksforgeeks.org/python-string-strip/

#   * Title    : Remove spaces from a string in Python
#   * Author   : GeeksForGeeks.org
#   * Date     : 2025-04-17
#   * Accessed : 2025-05-20
#   * URL      : https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/

import string
import Question_4_isPalindrome as is_palindrome_module

def main():
    print("---------- Palindrome checker ----------\n")
    while True:
        # Remove leading or trailing whitespace and convert letters to lower case.
        word = input("Please enter a word (or 'exit' to quit): ").strip().lower()
        if word == 'exit':
            print("Exiting the palindrome checker.")
            break
        if not word:
            print("\n - You entered an empty string, please enter a valid word.")
            continue
        
        # Remove all spaces
        word = word.replace(" ", "")
        
        # Remove all punctuation
        word = word.translate(str.maketrans('', '', string.punctuation))
        
        # I chose traditional palindromes (only letters) and not numberic or alphanumberic palindromes.
        # Check if the word conatins only letters.
        if not word.isalpha():
            print("\n - Please enter a word containing only letters.\n")
            continue
    
        if is_palindrome_module.is_palindrome(word):
            print(f"\n - The word '{word}' is a palindrome.\n")
        else:
            print(f"\n - The word '{word}' is not a palindrome.\n")
        
if __name__ == "__main__":
    main()