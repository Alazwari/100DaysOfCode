#Day 44


class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        print(f'{name} thing is {model}, and its color is {color}.')

first_car = Car('First', 'BMW', 'Black')
second_car = Car('Second', 'Nisan', 'White')

class Jet(Car):
    def __init__(self, name, model, color):
        super().__init__(name, model,color)
        self.year = 2020
        print(f'The year is {self.year}')

first_jet = Jet('ABC','123','White')
