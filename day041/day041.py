#Day 041

class Greet:
    def __init__(self, name):
        self.name = name
    
    def work(self):
        self.job = input(f'Hello {self.name}, what is your job?')
        print(f'{self.name}, ====> {self.job}')

first = Greet('Abdulrahman')
first.work()

second = Greet('Mohammed')
second.work()