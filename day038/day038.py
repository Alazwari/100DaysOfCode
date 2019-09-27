# Dau 38

# List comprehensions
numbers = [23,53,654,-99,3452,-3]
new_numbers = [num / 2 if num > 0 else 0 for num in numbers]
print(new_numbers)

order_numbers = {x:y for x,y in zip(range(len(new_numbers)),new_numbers)}
print(order_numbers)