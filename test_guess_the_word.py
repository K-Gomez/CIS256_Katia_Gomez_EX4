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
    random_movie = random.choice(disney_movies)
    letter_list = list(random_movie)
    print("Guess the name of the Disney movie!\n")
    print(f"The name of this movie has {len(random_movie)} letters.\n")
    
    word_completion = 0
    while word_completion != len(random_movie):
        letter_guessed = input("Enter the letter you would like to guess:")
        # It letter is in word, display letters completed and add count to workd completion

        # If lettet is not there, prompt user to try agai



    print(random_movie)
    print(letter_list)


play_game()