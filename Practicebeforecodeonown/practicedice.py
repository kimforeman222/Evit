''' I want to make a dice. Users can choose the size of the dice.
The dice can either be 4 sided or 6 sided.
name variables such as sides of dice, integers
write a list- randomize the sides user could roll
loop this everytime the user wants to roll the dice.
if the user types roll the program randomizes a number
if the user'''
import random

'''dice1 = [1,2,3,4]
dice2 = [1,2,3,4,5,6]
userchooses = input("Which dice do you want to choose? Choose between 1 and 2\n")'''
def roll_dice():
    return random.randint(1,1000)

def main():
    print("WELCOME TO KIMS LUCKY DICE ROLLER")
    while True:
        roll = input("Type 'roll' to roll the dice or 'stop' to exit the web:\n")
        if roll == 'roll':
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif roll == 'quit':
            print("Thanks for playing!<3")
            break
        else:
            print("Sorry! Invalid! Please try again:)")
if __name__ == "__main__":
    main()