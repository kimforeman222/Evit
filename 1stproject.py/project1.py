'''Load digital dictionary file as a list of words
Accept a word from user
Create an empty list to hold anagrams
Sort the user-word
Loop through each word in the word list: 
    Sort the word
    if word sorted is equal to user-word sorted:
            Append word to anagrams list
Print anagrams list'''
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
anagram_list = {}
name = 'Foster'
print ("Input name = {}".format (name))
name = name.lower()
print("Using name = {}".format(name))

'''sort names and find anagrams'''
print()
if len(anagram_list) ==0:
        print ("You need a larger dictionary or a new name!")
else: 
        print("Anagrams =", *anagram_list, sep='\n')
    
name= 'foster'
word = 'forest'
name_count = Counter(name)
print(name_count)
Counter ({'f': 1, 't': 1, 'e': 1, 'o': 1, 'r': 1, 's': 1})
word_count = Counter(word)
print(word_count)
Counter({'f': 1, 't': 1, 'o': 1, 'e': 1, 'r': 1, 's': 1})
if word_count == name_count:
        print("It's a match")

import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('2of4brif.txt')
dict_file.append('a')
dict_file.append('i')
dict_file= sorted(dict_file)

ini_name = input("Enter a name:")

def find_anagrams(name, word_list):
        '''Red name and dictionary file and display all anagrams IN name.'''
        name_letter_map = Counter(word.lower())
        for word in word_list:
                test = ''
                word_letter_map = Counter(word.lower())
        for letter in word:
                if word_letter_map[letter]:
                        test += letter
                elif Counter(test) == word_letter_map:
                        find_anagrams.append(word)

print(*find_anagrams, sep= '\n')
print()
print("Remaining letters = {}".format(name))
print("Number of remaining letters = {}". format(len(name)))
print("Number of remaining (real word) anagrams = {}".format(len(run)))

def choice(name):
        """Check user choice for validity, return choice and leftover letters."""
        while True:
                choice == input ('\nMake a choice else Enter to start over or $ to end:')
if choice == '':
        main()
elif choice == '#':
        sys.exit()
else:
        candidate= ''.join(choice.lower(),split())
left_over_list =list(name)
for letter in candidate:
        if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
                break
else:
        print("Won't work! Make another choice!:", file=sys.stderr)
name = ''.join(left_over_list) # makes display more readable


def main():
        '''help user build anagram phrase from their name'''
name = ''.john(ini_name.lower().split())
name = name.replace('-','')
limit = len(name)
phrase = ''
running = True

while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
                print("Length of anagram phrase = {}".format(len()))

find_anagrams(name, dict_file)
print("Current anagram phrase =", end= " ")
print(phrase, file=sys.stderr)


phrase += choice + ' '

if len(temp_phrase) == limit:
        print("\n****FINISHED!!!****\n")
        print("Anagram of name =", end= " ")
        print(phrase, file=sys.stderr)
        print()
        try_again = input('\n\nTry again? (Press Enter else "n" to quit)\n')
if try_again.lower() == "n":
        running = False
        sys.exit()
else:
        main()
if __name__ == '__main__':
        main()