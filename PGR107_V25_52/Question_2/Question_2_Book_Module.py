#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 12:22:07 2025

@author: Candidate 52
"""

class Book:
    def __init__(self, title, author, num_pages, borrowed = False):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.borrowed = borrowed
        
    def __str__(self):
        return (
        f"Book Details:\n"
        f"  Title: '{self.title}'\n"
        f"  Author: {self.author}\n"
        f"  Pages: {self.num_pages}\n"
        f"  Borrowed: {self.borrowed}\n"
        )