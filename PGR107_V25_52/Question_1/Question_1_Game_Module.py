#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 14:59:11 2025

@author: Candidate 52
"""

import random

class WordGuessingGame:
    def __init__(self):
        self.current_guess = ""
        self.already_guessed  = []
        self.random_word = self.__get_word()
        self.guesses_left = len(self.random_word)
        
        # Each letter by itself in an array/list, so that we know the index of each letter
        self.characters = list(self.random_word)
        
        # In a new array, store a underscore for each letter in the characters array
        self.underscores = ['_' for character in self.characters]
    
    def __get_word(self):
        try:
            # Open file and put the content in a usable variable
            with open('words.txt', 'r') as word_file:
                content = word_file.read()
                if not content:
                    print("The word file is empty.")
                    exit()
                word = content.split(', ')
                random_word = random.choice(word)
                return random_word
        except FileNotFoundError:
            print("Error: The file was not found.")
            exit()
            
    def get_user_guess(self):
        while True:
            guess = input("Guess a character: ").lower()
            if(len(guess) == 1 and guess.isalpha()):
                self.current_guess = guess
                break
            print("\nInvalid input! Please enter a single alphabetic character.\n")
            
    def handle_guess_attempt(self):
        self.already_guessed.append(self.current_guess)
        
        if self.current_guess in self.random_word:
            self.__add_correct_guess()
            return True
        else:
            self.guesses_left = self.guesses_left - 1
            return False
            
    # Print out underscores nicely and not in array format
    def print_underscores(self):
        for character in self.underscores:
            print(character, end=" ")
        print("\n")
    
    def get_word_length(self):
        return len(self.random_word)
    
    def get_remaining_guesses(self):
        return self.guesses_left
    
    def __add_correct_guess(self):
        
        # Store the index number of all letters
        indexes = []
        
        # Iterate the characters list using enumerate to get both index and element
        for index, character in enumerate(self.characters):
            
            # If current character matches the guessed character, add its index to the list of indexes
            if character == self.current_guess:
                indexes.append(index)
                
        # For every index that was saved in the indexes array, change the current underscore with the guess by the given index
        for index in indexes:
            self.underscores[index] = self.current_guess