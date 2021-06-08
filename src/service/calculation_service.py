"""Module for the CalculationService class"""
from tkinter import StringVar
import divide_service as divide_service
import multiply_service as multiply_service


class CalculationService:
    """""Class for keeping track of, and evaluating calculations"""""

    # Constructor for the class
    # Initializes a String expression and a StringVar equation
    # StringVar is used because it is required for the tkinter text box
    def __init__(self):
        print("initialized")
        self.expression = ""
        self.equation = StringVar()

    def press(self, num):
        """Function to update the expression in the text entry box"""
        # appends the new number to the existing expression
        self.expression = self.expression + str(num)

        # update the expression by using set method
        self.equation.set(self.expression)

    def equalpress(self):
        """Function to evaluate the final expression"""

        # using a try/except in order to catch errors
        try:

            # evaluate the expression/calculation
            if "/" in self.expression:
                total = str(divide_service.divide(self.expression))
            if "*" in self.expression:
                total = str(multiply_service.multiply(self.expression))
            else:
                total = str(eval(self.expression))
               

            if float(total) > 10:
                total = total + " <:o)"

            self.equation.set(total)

            # reset the expression to the empty string
            self.expression = ""

        # show error on the screen after an exception is caught
        except:
            self.equation.set(" error ")
            self.expression = ""



    def clear(self):
        """Function to clear the contents of text entry box"""
        self.expression = ""
        self.equation.set("")

    def get_expression(self):
        """get expression"""
        return self.expression

    def set_expression(self, newExpression):
        """set expression"""
        self.expression = newExpression

    def get_equation(self):
        """get equation"""
        return self.equation

    def set_equation(self, new_equation):
        """set equation"""
        self.equation.set(new_equation)
