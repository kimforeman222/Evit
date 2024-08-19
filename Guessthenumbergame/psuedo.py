# need to import a library, (random) which holds a range of numbers 1-100
# generate a random number within the range
# store the generated number as the target number
# initialize the number of attempts to 0
# While the user hasn't guessed the correct number:
# Prompt the user to enter a guess.
# Increment (put in) the attempt counter.
# Compare Guess to Target Number:
# if the guess is equal to the target number
# congragulate the user and display number of attempts
# end game
'''If the guess is less than the target number:
Inform the user that the guess is too low.
If the guess is greater than the target number:
Inform the user that the guess is too high.
'''
#offer the user an option to play again or quit
# if the user chooses to play again, restart the game loop
# if the user chooses to quit, thank them for playing and end the prgram
import tkinter as tk

'''def main():
    root = tk.Tk()
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()    '''

import random
GenerateRandomNumber="[min,max]"
min_val = 0
max_val = 100
target_number = random.randint(min_val, max_val)
print ("The target number is", target_number)
# Let players know their objective
title = "\nI'm thinking of a number between {} and {}! Try to guess...".format(min_val, max_val)
print(title)
attempts = 0
# Set up game
while True:
    # Prompt the user to make a guess
    human_guess = int(input("Enter your guess: "))
    
    # Increment the attempt counter
    attempts += 1

    # Check if the guess is correct
    if human_guess == target_number:
        print("Congratulations! You guessed the number in {} attempts.".format(attempts))
        break
    elif human_guess < target_number:
        print("Too low! Try again.")
    elif human_guess > target_number:
        print("Too high! Try again.")
    else: 
        print("Please input a number")

while True:
    # Prompt the user to make a guess
    try:
        human_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
