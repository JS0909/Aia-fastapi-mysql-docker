from app.models.calculator import Calculator

class CalculatorService(object):
    def __init__(self)->None: 
        pass

    def calculate(self, first, second):
        calc =  Calculator(first, second)
        print(f'첫번째수: {calc.first}')
        print(f'첫번째수: {calc.second}')
        print(f'{calc.first} + {calc.second} = {calc.sum()}')
        print(f'{calc.first} - {calc.second} = {calc.subtract()}')
        print(f'{calc.first} * {calc.second} = {calc.multiple()}')
        print(f'{calc.first} / {calc.second} = {calc.divide()}')