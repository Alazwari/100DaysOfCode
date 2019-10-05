#Day 043

#Day 42

class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        print(f'{name} car is {model}, and its color is {color}.')

first_car = Car('First', 'BMW', 'Black')
second_car = Car('Second', 'Nisan', 'White')

class Jet(Car):
    pass

first_jet = Jet('ABC','123','White')