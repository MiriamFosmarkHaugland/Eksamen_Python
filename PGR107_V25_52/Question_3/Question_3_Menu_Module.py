#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 20:11:26 2025

@author: Candidate 52
"""

class Menu:
    def __init__(self):
        self.menu_List = []
        
    def add_option(self, option):
        self.menu_List.append(option)
    
    def get_input(self):
        for option in self.menu_List:
            print(option)
            
        menu_choice = input("Choice: ")
        return menu_choice