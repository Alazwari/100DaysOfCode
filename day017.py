#Day 17
import string
import random

def passowrd(length = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(length))

print(passowrd(int(input('How many characters in your password?'))))