#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

word1 = str(input("Enter a word: ")).strip()
word2 = str(input("Enter a word: ")).strip()
word3 = str(input("Enter a word: ")).strip()
word4 = str(input("Enter a word: ")).strip()
word5 = str(input("Enter a word: ")).strip()

myList = [word1, word2, word3, word4, word5]

print(myList)