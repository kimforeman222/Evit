import sys 
import random
print("Welcome to the 'Silly Pet Names Generator.' \n")
print("This is where all your confusion ends! \n" )

first_names = ('Abigail', 'Ace', 'Adam','Addie','Admiral','Aggie','Aires','Aj','Jax','Aldo','Alex','Alexus','Alf','Alfie','Allie','Ally','Amber','Amie','Amigo','Amos','Amy','Andy','Angel','Angus','Annie','Apollo','April','Archie','Argus','Aries')

last_names = ('Armanti','Arnie','Arrow','Ashes','Ashley','Astro','Atlas','Audi','Augie','Aussie','Austin','Autumn','Axel','Babe','Baby','Baby-doll','Babykins','Bacchus','Bailey','Bam-bam','Bandit','Banjo','Barbie','Barclay','Barker','Barkley','Barley','Barnaby','Barney','Baron','Bart','Basil','Baxter','Bb','Beamer','Beanie','Beans','Bear','Beau','Beauty','Beaux')

while True:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    print("\n\n")
    print("{} {}".format(first_name, last_name))
    print("\n\n")

    try_again = input("Try again? (Press Enter else 'n' to quit): ").strip().lower()
    if try_again == "n":
        break

input("Press Enter to exit")