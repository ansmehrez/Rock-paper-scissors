# Start game: print welcome to game Rock paper scissors
print("Welcome to the game 'Rock paper scissors'")

# Input choice: your move (Rock paper scissors)
user = input("Choose a move from 'Rock', 'Papers', 'Scissors': ").capitalize()
print("User choice: " + user)

# Make random move (Rock paper scissors)
import random
pc = random.choice(["Rock", "Papers", "Scissors"])
print("PC choice: " + pc)

# Make if statement
if pc == user:
    print("That's a draw, try again")
elif (user == 'Papers' and pc == 'Rock') or (user == 'Rock' and pc == 'Scissors') or (user == 'Scissors' and pc == 'Papers'):
    print("You win!")
else:
    print("You lose!")
 


