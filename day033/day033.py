# Day 33
def rec(x):
    if x > 0:
        result = x + rec(x-1)
    else:
        result = 0
    return result

print(rec(3))