import random

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

    print("Guess the name of the Disney movie!\n")
    print(f"The name of this movie has {len(random_movie)} letters.\n")

    print(random_movie)
    print(letter_list)
    
    word_completion = 0
    guessed_letters = set()

    while word_completion != word_length:
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
        print(guessed_letters)
        guess = input("Enter the letter you would like to guess: ")       
        letter_guessed = guess.lower()
       

        if letter_guessed in guessed_letters:
            print("You already guessed that letter!\n")
        
        # It letter is in word, display letters completed and add count to word completion
        if letter_guessed in letter_list:
            print("Correct!")
            guessed_letters.add(letter_guessed)
            word_completion = word_completion + random_movie.count(letter_guessed)
                     
        # If letter is not there, prompt user to try again
        else:
            print("Try again!")
            guessed_letters.add(letter_guessed)


    print("Congratulations! You won!")
    print(f"The movie name of the movie is {movie}!")
    

play_game()