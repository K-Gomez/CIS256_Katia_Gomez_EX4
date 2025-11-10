# Katia Gomez
# CIS256 Fall 2025
# EX 4 - Test File

import random
from guess_the_word import disney_movies
import pytest

"""
Test file for guess_the_word.py
Tests random word selection and letter guessing logic
"""

def test_random_word_selection():
    chosen_word = random.choice(disney_movies)
    assert chosen_word in disney_movies

def test_correct_quess_processing():
    word = "brave"
    guessed_letters = {"b"}
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    assert display_word == "b____"

def test_incorrect_guess_processing():
    word = "brave"
    guessed_letters = {"z"}
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    assert display_word == "_____"