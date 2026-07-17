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
