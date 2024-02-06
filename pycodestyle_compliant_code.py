#!/usr/bin/env python3

"""Simple Calculator module"""


class Calculator:
    """Performs simple calculations ie addition, subtruction, multiplication
    and division"""
    def __init__(self, num1, num2):
        """initializes first and second number"""
        self.n1 = num1
        self.n2 = num2

    def add(self):
        """Adds two numbers"""
        return self.n1 + self.n2

    def sub(self):
        """subtruct two numbers"""
        return self.n1 - self.n2

    def mul(self):
        """multiply two numbers"""
        return self.n1 * self.n2

    def div(self):
        if self.n2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.n1 / self.n2


if __name__ == "__main__":
    mycalc = Calculator(40, 0)
    print(mycalc.add())
    print(mycalc.div())
