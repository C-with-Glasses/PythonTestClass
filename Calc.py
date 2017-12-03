#!/usr/local/bin/python3.6

class Calc:
    def calc_add(num1, num2):
        total = num1 + num2
        print(total)

    def calc_sub(num1, num2):
        total = num1 - num2
        print(total)

    def calc_mult(num1, num2):
        total = num1 * num2
        print(total)

    def calc_div(num1, num2):
        total = num1 / num2
        print(total)

    
class Main:
    print("\t\tWelcome to Calc!\n\n")

    while True:
        num1 = int(input("Enter a number: "))
        
        choice_input = input("+, -, x, or % ")

        num2 = int(input("Enter a number: "))

        if choice_input == "+":
            Calc.calc_add(num1, num2)
            break
        if choice_input == "-":
            Calc.calc_sub(num1, num2)
            break
        if choice_input == "x":
            Calc.calc_mult(num1, num2)
            break
        if choice_input == "%":
            Calc.calc_div(num1, num2)
            break
