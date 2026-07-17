class CalculatorManager:

    def __init__(self):
        self.calculator_history = []

    # Method to show calculator menu
    def see_menu(self):
        print("="*35)
        print("            CALCULATOR MENU")
        print("="*35)
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Find Square")
        print("7.Find Cube")
        print("8.View calculator history")
        print("9.Clear calculator history")
        print("10.See calculator menu")
        print("11.Back")

    # Method to calculate the summation of numbers
    def addition(self):
        while True :
            expression = input("Enter the expression :")
            if (not expression):
                print("The expression is empty")
                return None
            elif (expression.startswith("+") ):
                print("The expression should not starts with "+" ")     
                return None   
            elif (expression.endswith("+")):
                print("The expression should not ends with "+" ")     
                return None       
            elif ("++" in expression):
                print("The expression should not contain "++"")
                return None        
            else:
                numbers = expression.split("+")

                for num in numbers:
                    if not num.isdigit():
                        print("Expression should contain only numbers.")
                        return

                numbers = [int(num) for num in numbers]

                total = sum(numbers)
                calculator_record = {
                    "operation" : "Addition",
                    "expression" : expression,
                    "answer" : total 
                }
                self.calculator_history.append(calculator_record)


                print("The sum of all numbers is:", total)
                self.battery = self.battery - 2
                return
