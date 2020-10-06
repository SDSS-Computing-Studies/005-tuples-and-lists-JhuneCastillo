#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

listName = ["Alain", "Brian", "Chris", "Justin", "Angela", "Rick"]
print(listName)

replaceName = str(input("Choose a person from list to replace: ")).strip()

replacementName = str(input("Enter the replacement: ")).strip()

index = listName.index(replaceName)
listName.remove(replaceName)
listName.insert(index, replacementName)

print(listName)