#! python3
"""
Sort the given list by numerical value
Find the smallest and the largest value and display them:

inputs:
none

outputs:
string containing the 2 numbers:

example:
The smallest number is 3 and the largest number is 9
"""

myList = [ 3,6,5,4,6,7,8,6,5,9,4,5 ]

x = str(min(myList))
y = str(max(myList))

print("The smallest number is " + x + " and the largest number is " + y)