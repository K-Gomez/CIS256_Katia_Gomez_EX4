# Katia Gomez
# CIS256 Fall 2025
# EX 3.2

"""
Implement the game with the following features:
Select a random word from a predefined list.
Prompt the user to guess one letter at a time.
Reveal letters if the guess is correct; indicate if incorrect.
Continue until the user guesses the word or runs out of attempts.
Display a congratulatory message when the word is guessed.
"""

import os
import time

# Function to clear the console screen
def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS and Linux
    else:
        os.system('clear')

# Initialize list disney movies with single word titles
disney_movies = [
    "Bambi",
    "Dumbo",
    "Aladdin",
    "Mulan",
    "Hercules",
    "Cinderella",
    "Brave",
    "Up",
    "Pinocchio",
    "Fantasia",
    "Atlantis",
    "Pocahontas",
    "Flubber",
    "Tarzan",
    "Fantasia",
    "Dinosaur",
    "Moana",
    "Onward",
    ]

