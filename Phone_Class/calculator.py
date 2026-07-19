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

    # Method to calculate the multiplication of numbers
    def multiplication(self):
        while True :
            expression = input("Enter the expression :")
            if (not expression):
                print("The expression is empty")
                return None
            elif (expression.startswith("*") ):
                print("The expression should not starts with "*" ")     
                return None   
            elif (expression.endswith("*")):
                print("The expression should not ends with "*" ")     
                return None       
            elif ("**" in expression):
                print("The expression should not contain "**"")
                return None        
            else:
                numbers = expression.split("*")

                for num in numbers:
                    if not num.isdigit():
                        print("Expression should contain only numbers.")
                        return

                numbers = [int(num) for num in numbers]

                total = 1
                for number in numbers :
                    total = total * number

                calculator_record = {
                    "operation" : "Multiplication",
                    "expression" : expression,
                    "answer" : total 
                }
                self.calculator_history.append(calculator_record)                

                print("The multiplication is :", total)
                self.battery = self.battery - 2 
                return

    # Method to calculate the subtraction of numbers
    def subtraction(self):
        while True :
            expression = input("Enter the expression :")
            if (not expression):
                print("The expression is empty")
                return None
            elif (expression.startswith("-") ):
                print("The expression should not starts with "-" ")     
                return None   
            elif (expression.endswith("-")):
                print("The expression should not ends with "-" ")     
                return None       
            elif ("--" in expression):
                print("The expression should not contain "--"")
                return None        
            else:
                numbers = expression.split("-")

                for num in numbers:
                    if not num.isdigit():
                        print("Expression should contain only numbers.")
                        return

                numbers = [int(num) for num in numbers]

                total = numbers[0]                
                for j in range (1,len(numbers)):
                    total = total - numbers[j]
                print("The subtraction of numbers is :", total)   
                self.battery = self.battery - 2
                

                calculator_record = {
                    "operation" : "Subtraction",
                    "expression" : expression,
                    "answer" : total 
                }
                self.calculator_history.append(calculator_record)  
                return              

    # Method to calculate the division of numbers
    def division(self):
        while True:
            num1=input("Enter the first number :")
            if(num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("Number should be a digit")
        while True:
            num2 = input("Enter the second number :")
            if(num2.isdigit()):
                num2=int(num2)
                if (num2 != 0):
                    total = (num1 / num2)
                    print("The division of numbers is :" , total)
                    expression = f"{num1}/{num2}"
                    calculator_record = {
                    "operation" : "Division",
                    "expression" : expression,
                    "answer" : total 
                }
                    self.calculator_history.append(calculator_record)                

                    self.battery = self.battery - 2
                    return
                else:
                    print("Error : Cannot divide by zero.")
            else:
                print("Number should be a digit")   

    # Method to find the remainder of numbers
    def modulus(self):
        while True:
            num1=input("Enter the first number :")
            if(num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("Number should be a digit")
        while True:
            num2 = input("Enter the second number :")
            if(num2.isdigit()):
                num2=int(num2)
                if (num2 != 0):
                    total = (num1 % num2)
                    print("The modulus of numbers is :" , total)
                    expression = f"{num1}%{num2}"
                    calculator_record = {
                    "operation" : "Modulus",
                    "expression" : expression,
                    "answer" : total 
                }
                    self.calculator_history.append(calculator_record)  
                    self.battery = self.battery - 2
                    return
                else:
                    print("Error : Number can not be zero.")
            else:
                print("Number should be a digit")  

    # Method to find the square of a number
    def square(self):
        while True:
            number = input("Enter the number to find square :")
            if (number.isdigit()):
                number = int(number)
                total = (number * number)
                print("The square is :" , total)
                expression = f"{number}*{number}"
                calculator_record = {
                    "operation" : "Square",
                    "expression" : expression,
                    "answer" : total 
                }
                self.calculator_history.append(calculator_record)  

                self.battery = self.battery - 2
                return
            else:
                print("Number should be a digit")     

    # Method to find the cube of a number
    def cube(self):
        while True:
            number = input("Enter the number to find cube :")
            if (number.isdigit()):
                number = int(number)
                total = (number * number * number)
                print("The cube is :" , total)
                expression = f"{number}*{number}*{number}"
                calculator_record = {
                    "operation" : "Cube",
                    "expression" : expression,
                    "answer" : total 
                }
                self.calculator_history.append(calculator_record)  
                self.battery = self.battery - 2
                return
            else:
                print("Number should be a digit")  

    # Method to view the calculator history    
    def view_calculator_history(self):
        if ( not self.calculator_history):
            print("=============================")
            print("Calculator history is empty")
            print("=============================")
        else:
            print()
            print("="*35)   
            print("            CALCULATOR HISTORY") 
            print("="*35)
            for index , calculation in enumerate(self.calculator_history, start=1):
                print(f"Calculation {index}")
                print(f"Operation   : {calculation['operation']}")
                print(f"Expression : {calculation['expression']}")
                print(f"Answer      : {calculation['answer']}")
                print("-" * 35)  
