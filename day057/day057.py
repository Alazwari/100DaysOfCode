# Day 57
import re

text = "Python is an easy programing language"
x = re.search("^Python.*language$", text)

if x:
    print('Match')
else:
    print('No  match')