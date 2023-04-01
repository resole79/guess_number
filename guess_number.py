from art import logo
import random

# Declare Variable
numb1 = 1
numb2 = 100


# Function to guess a number
def guess_number(level, number):
    """
    Function to guess a number
    accept:
    level -> string (easy, hard)
    number -> int
    """
    # Declare variable
    game_over = False

    if level == "hard":
        attempt = 5
    else:
        attempt = 10

    # Cycle while condition to exit attempt equal at 0 and the game is over
    while attempt != 0 and not game_over:
        player_guess = ""

        print(f"You have {attempt} attempts remaining to guess the number")

        while not player_guess.isnumeric():
            player_guess = input("Make a guess: ")
            while player_guess.isnumeric():
                if int(player_guess) > numb2:
                    player_guess = input("Make a guess: ")
                else:
                    break
            else:
                player_guess = input("Make a guess: ")

        player_guess = int(player_guess)

        if player_guess == number:
            print(f"Congratulation, you got it")
            game_over = True
        elif player_guess > number:
            print("Too High\nGuess again")
            attempt -= 1
        else:
            print("Too Low\nGuess again")
            attempt -= 1

        if attempt == 0:
            print(f"\nYou've run out of guess, you Lose!\nThe answer was {number}")
            game_over = True


# Function game
def game():

    play_again = True

    while play_again:
        # Declare Variable
        continue_to_play = ""
        difficulty = ""

        # Call function randint from import random method
        num_to_guess = random.randint(numb1, numb2)

        print(logo)

        print("Welcome to the Number Guessing Game")
        print(f"I'm thinking of a number between {numb1} and {numb2}")

        # Cycle "while" condition to exit "difficulty" equal to "easy" or "hard"
        while difficulty != "easy" and difficulty != "hard":
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ")

        # Call function "guess_number"
        guess_number(difficulty, num_to_guess)

        # Cycle "while" condition to exit "continue_to_play" equal to "y" or "n"
        while continue_to_play != "y" and continue_to_play != "n":
            continue_to_play = input("\nDo you want to continue to play? ( Y/N ) ").lower()

        if continue_to_play == "y":
            play_again = True
        elif continue_to_play == "n":
            print("GoodBye")
            break


# Call function "game"
game()
