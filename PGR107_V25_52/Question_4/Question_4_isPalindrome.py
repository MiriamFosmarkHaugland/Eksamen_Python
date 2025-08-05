#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 14:42:24 2025

@author: Candidate 52
"""

def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True