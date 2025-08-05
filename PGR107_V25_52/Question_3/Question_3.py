#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 11:11:05 2025

@author: Candidate 52
"""

import Question_3_Menu_Module as menu_module        
import Question_3_BankAccount_Module as bank_account_module

def main():
    menu_instance = menu_module.Menu()
    bank_account_instance = None
    
    menu_instance.add_option("> (1) Open a new account")
    menu_instance.add_option("> (2) Deposit money into your account")
    menu_instance.add_option("> (3) Withdraw money from your account")
    menu_instance.add_option("> (4) Add interest to your account")
    menu_instance.add_option("> (5) Get the current balance of your account")
    menu_instance.add_option("> (6) Quit")
    
    while True:
        menu_choice = menu_instance.get_input()
        
        if menu_choice == "1":
            interest_rate = 0.05
            bank_account_instance = bank_account_module.BankAccount(0, interest_rate)
            print("\n - New account created.\n")
            
        elif menu_choice == "2":
            if bank_account_instance:
                try:
                    balance = bank_account_instance.get_balance()
                    print(f"Current balance is {balance}$")
                    deposit_amount = float(input("Amount you want to deposit: "))
                    if deposit_amount <= 0:
                        print("\n - You cannot deposit a negative number or nothing.\n")
                    else:
                        bank_account_instance.deposit(deposit_amount)
                        print(f"\n - Successfully deposited: {deposit_amount}$\n")
                except ValueError:
                    print("\n - Invalid amount, please enter a number.\n")
            else: print("\n - Please open a new account first.\n")
            
        elif menu_choice == "3":
            if bank_account_instance:
                try:
                    balance = bank_account_instance.get_balance()
                    print(f"Current balance is {balance}$")
                    withdraw_amount = float(input("Amount you want to withdraw: "))
                    if withdraw_amount <= 0:
                        print("\n - You cannot withdraw a negative number or nothing.\n")
                    elif withdraw_amount > balance:
                        print("\n - You cannot withdraw more than your current balance.\n")
                    else:
                        bank_account_instance.withdraw(withdraw_amount)
                        print(f"\n - Successfully withdrawn: {withdraw_amount}$\n")
                except ValueError:
                    print("\n - Invalid input, please enter a number.\n")
            else: print("\n - Please open a new account first.\n")
            
        elif menu_choice == "4":
            if bank_account_instance:
                interest = bank_account_instance.add_interest()
                print(f"\n - Successfully added interest: {interest:.2f}$\n")
            else: 
                print("\n - Please open a new account first.\n")
            
        elif menu_choice == "5":
            if bank_account_instance:
                balance = bank_account_instance.get_balance()
                print(f"\n - Current balance is {balance}$\n")
            else: 
                print("\n - Please open a new account first.\n")
            
        elif menu_choice == "6":
            print("\n - Logging out.")
            break
        else:
            print("\n - This is not a valid menu choice, please try again.\n")
    
    
if __name__ == "__main__":
    main()