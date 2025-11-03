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

# Import Modules
import os
import time
import random


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
    "Onward"
    ]


def play_game():
    movie = random.choice(disney_movies)
    random_movie = movie.lower()
    
    letter_list = list(random_movie)
    word_length = len(random_movie)
                
    word_completion = 0
    guessed_letters = set()

    while word_completion != word_length:
        
        print("Guess the name of the Disney movie!\n")
        print(f"The name of this movie has {len(random_movie)} letters.\n")

        display_word = ""
        for letter in random_movie:
            if letter == " ":
                display_word += " "

            elif letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("Current word: ", display_word)
            
        print("Letters Used: ")   
        print(sorted(guessed_letters))
        guess = input("Enter the letter you would like to guess: ")       
        letter_guessed = guess.lower()
       
        if letter_guessed in guessed_letters:
            print("You already guessed that letter!\n")
            clear_console()
        
        # It letter is in word, display letters completed and add count to word completion
        if letter_guessed in letter_list:
            print("Correct!")
            guessed_letters.add(letter_guessed)
            word_completion = word_completion + random_movie.count(letter_guessed)
            clear_console()
                     
        # If letter is not there, prompt user to try again
        else:
            print("Try again!")
            guessed_letters.add(letter_guessed)
            clear_console()

    print("Congratulations! You won!")
    print(f"The movie name of the movie is {movie}!")  



# Method to display the main menu and allow user to navigate system functions
def main_menu():
# Loop continues until the user chooses to exit
    while True:
        clear_console() # Clear screen at the start of each loop

        # Display welcome message
        print("Guess the movie!\n")
    
        # Explain how to navigate the menu
        print("Enter the number of the desired menu option.")
        print("Press the Enter key after entering the number.")
        print("-" * 30)
        print("Main Menu")
        print("-" * 30)
        print( "\n"
            "   1 - Start Game \n"
          
            "   2 - Exit the program \n")
        print("-" * 30)

        selection = input("Choice: ")

        # Match user input to the corresponding feature
        if selection == '1':
            clear_console()
            play_game()
            input("\nPress Enter to return to the main menu...")

        elif selection == '2':
            print("Thank you for visiting! Goodbye!")
            time.sleep(1)  # Pause for 1 second before exit
            clear_console()
            break # If user enters "4" loop breaks and ends program
        else:
            print("Please enter a valid selection. ")  # Handle invalid inputs
            time.sleep(1)  # Pause briefly before reloading menu



# Main Program Execution

# Clear screen before starting program
clear_console()  

# Call the main menu function to start the program
main_menu()
