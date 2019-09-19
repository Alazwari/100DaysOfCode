# Day 31

numbers = range(1,20)
def odd_even(num):
    for num in numbers:
        print(f'{num} is even') if num % 2 == 0 else print(f'{num} is odd')

odd_even(numbers)