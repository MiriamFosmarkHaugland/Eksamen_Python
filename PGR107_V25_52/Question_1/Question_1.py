#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 10 09:58:10 2025

@author: Candidate 52
"""

# SOURCES

#   * Title    : With statement in Python
#   * Author   : GeeksForGeeks.org
#   * Date     : 2025-03-03
#   * Accessed : 2025-05-10
#   * URL      : https://www.geeksforgeeks.org/with-statement-in-python/

#   * Title    : Python string split()
#   * Author   : GeeksForGeeks.org
#   * Date     : 2025-04-02
#   * Accessed : 2025-05-10
#   * URL      : https://www.geeksforgeeks.org/python-string-split/

#   * Title    : Split string into list of characters in Python
#   * Author   : GeeksForGeeks.org
#   * Date     : 2025-04-19
#   * Accessed : 2025-05-10
#   * URL      : https://www.geeksforgeeks.org/python-string-split/

#   * Title    : Enumerate() in Python
#   * Author   : GeeksForGeeks.org
#   * Date     : 2025-01-20
#   * Accessed : 2025-05-11
#   * URL      : https://www.geeksforgeeks.org/enumerate-in-python/


import Question_1_Game_Module as game_module
            
def main():
    game = game_module.WordGuessingGame()
    
    print("----- Welcome to the Word Guessing Game! -----\n")
    
    print(f"The word you need to guess has '{game.get_word_length()}' characters." )
    print(f"You have {game.get_word_length()} guesses.")
    
    while game.get_remaining_guesses() > 0:
        game.print_underscores()
        
        game.get_user_guess()
        
        # If the guess is not already guessed
        if game.current_guess not in game.already_guessed:
            
            # Check if the guess was right or wrong
            guessed_right = game.handle_guess_attempt()
            
            # If the guess is correct, print out a success message to the user.
            if guessed_right:
                print(" - Good job, that letter is in the word.")
                print(f" - You have {game.get_remaining_guesses()} guess(es) left.")
                
                print("---------------------------------------------")
                
                # If there are no more underscores in the array, the word is completed by the player
                if "_" not in game.underscores:
                    game.print_underscores()
                    print(f" - You found the word --> {game.random_word}")
                    print(" - Congratulation! you won.")
                    break
            else:
                # Otherwise print an unsuccess message to the user.
                print(" - Sorry, that letter is not in the word.")
                print(f" - You have {game.get_remaining_guesses()} guess(es) left.")
                print("---------------------------------------------")     
                
                # If the user has no more tries left, end the game
                if game.get_remaining_guesses() <= 0:
                    print(" - Sorry! you lost.")
                    print(f" - The word is --> {game.random_word}")
                    break
        else:
            print(" - Sorry, that letter is already guessed, try again.")
        
if __name__ == "__main__":
    main()