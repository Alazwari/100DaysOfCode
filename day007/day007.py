# Day 7

# String literals in python are surrounded by either single quotation marks,
#or double quotation marks.
print("Hello",end='') #double quotation marks
print(' World') #single quotation marks


#You can assign a multiline string to a variable by using three quotes.
#You can use three double quotes (""") Or three single quotes (''').
#(you can write whatever you want between the quotes).

"""
Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
"""

#Strings are Arrays
#Strings in Python are arrays of bytes representing Unicode characters.
#Python does not have a character data type, a single character is simply a string
#with a length of 1. Square brackets can be used to access elements of the string.


x = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
#Get the character at position 2
#(remember that the first character has the position 0).
print(x[1])
#Substring. Get the characters from position 5 to position 9 (not included)
print(x[5:9])
