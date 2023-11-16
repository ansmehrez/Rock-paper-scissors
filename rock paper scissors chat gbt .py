from termcolor import colored
import random

def print_welcome_message():
    print(colored("Welcome to the game 'Rock paper scissors'", 'green'))

def get_user_choice():
    return input("Choose a move from 'Rock', 'Paper', 'Scissors': ").capitalize()

def get_pc_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def display_choices(user, pc):
    print(f"User choice: {user}")
    print(f"PC choice: {pc}")

def determine_winner(user, pc):
    if user == pc:
        return "That's a draw, try again"
    elif (user == 'Paper' and pc == 'Rock') or (user == 'Rock' and pc == 'Scissors') or (user == 'Scissors' and pc == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print_welcome_message()

    while True:
        user = get_user_choice()
        pc = get_pc_choice()

        display_choices(user, pc)

        result_message = determine_winner(user, pc)
        print(result_message)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
