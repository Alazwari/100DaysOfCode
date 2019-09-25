# Day 36

def double_number(x):
    return lambda y : y * x
def tripler_number(x):
    return lambda y : y * x

double = double_number(2)
tripler = tripler_number(3)
print(double(24), tripler(13))