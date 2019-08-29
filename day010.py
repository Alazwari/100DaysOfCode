#Day 10

class operators:
    def __init__(self):
        print('''--------------------------------
sum(x, y) for +
sub(x, y) for -
div(x, y) for /
mul(x, y) for *
rem(x, y) for reminder
\n--------------------------------''')

    def sum(self, x, y): #دالة الجمع
        return x+y
    def sub(self, x, y): #دالة الطرح
        return x-y
    def div(self, x, y): #دالة القسمة
        return x / y
    def mul(self, x, y): #دالة الضرب
        return x * y
    def rem(self, x, y): #دالة باقي القسمة
        return x % y


operator = operators()

a = operator.sum(5, 6)
b = operator.sub(10, 5)
c = operator.div(20, 2)
d = operator.mul(3, 3)
e = operator.rem(10, 3)
print(a, b, c, d, e)