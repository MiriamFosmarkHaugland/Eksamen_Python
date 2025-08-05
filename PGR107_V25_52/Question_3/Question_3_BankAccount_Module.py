#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 20:14:15 2025

@author: Candidate 52
"""

class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        if amount > 0 and amount <=self.balance:
            self.balance -= amount
        return self.balance
        
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
        
    def get_balance(self):
        return self.balance