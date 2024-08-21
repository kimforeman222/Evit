import os
#practicing class making a data type for a specific character
#many attributes of the character are included here
class Character:
    def __init__(self, name, powertype, age, health, is_evil):
        self.name = name
        self.powertype = powertype
        self.age = age
        self.health = health
        is_evil = is_evil

character1 = Character("LANDENSLAYER", "Critical Damage", "20329", "300", "False")
character2 = Character("KIMPOSSIBLEBETTER", "Pink hacking", "16", "238348338", "True")
print(character2.powertype)

username = input("Please enter your username: ")
password = input("Please enter your password: ")


print(f"Please see your items down below {username}")
user_items = ["Sword", "Shield", "Potion", "Powerspell"]

for user_item in user_items:
    print(user_item)
def make_your_decision():
    print("Please make your choice of item")

make_your_decision()
decision = input("Choose an item from the list above: ")


def make_your_decision():
    decision = input("Choose an item from the list above: ")
    while decision not in user_items:
        print("SORRY item UNAVAILABLE")
        decision = input("Choose an item from the list above: ")
        break
    else: 
        print(f"CONGRATULATIONS you CHOSE {decision}")

items = 1
while items <= 10:
    print(items)
    items += 1

try:
    user_number_choice = int(input("Please choose a number between 1-10: "))
    print("Choose an item between 1-10")
except ValueError:
    print("INVALID TYPE A NUMBER")
    user_number_choice = int(input("Please choose a number between 1-10: "))
    print("Choose an item between 1-10")


character_accessories = [
    ["helmet", "chestplate","leggings", "boots"],
    ["steak", "chicken", "bread", "water"],
    ["picaxe", "axe", "hoe", "shears"],
]

for row in character_accessories:
    for col in row:
        print(col)

