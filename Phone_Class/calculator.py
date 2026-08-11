# Calculator manager class to perform arithmetic operations

from storage import save_calculations, load_calculations, save_battery

class CalculatorManager:

    # Constructor to initialize calculator history and battery manager
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager
        self.calculation_history = load_calculations()

    # Method to show calculator menu
    def see_calculator_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                 🧮 CALCULATOR                        ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. ➕ Addition                                      ║")
        print("║  2. ➖ Subtraction                                   ║")
        print("║  3. ✖️  Multiplication                                ║")
        print("║  4. ➗ Division                                      ║")
        print("║  5. 📊 Modulus                                       ║")
        print("║  6. 🔲 Find Square                                   ║")
        print("║  7. 🧊 Find Cube                                     ║")
        print("║  8. 📜 View Calculator History                       ║")
        print("║  9. 🗑️  Clear Calculator History                      ║")
        print("║ 10. 📋 Show Menu                                     ║")
        print("║ 11. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")


    # Method to calculate the summation of numbers
    def addition(self):
        while True:
            expression = input("➕ Enter the addition expression:\n")

            if (not expression):
                print("\n❌ Expression cannot be empty.\n")
                return None

            elif (expression.startswith("+")):
                print("\n❌ Expression should not start with '+'.\n")
                return None

            elif (expression.endswith("+")):
                print("\n❌ Expression should not end with '+'.\n")
                return None

            elif ("++" in expression):
                print("\n❌ Expression should not contain '++'.\n")
                return None

            else:
                numbers = expression.split("+")

                # Validate user input
                for num in numbers:
                    if not num.isdigit():
                        print("\n❌ Expression should contain numbers only.\n")
                        return

                numbers = [int(num) for num in numbers]

                total = sum(numbers)

                # Save the operation in history
                calculator_record = {
                    "operation": "Addition",
                    "expression": expression,
                    "answer": total
                }

                self.calculator_history.append(calculator_record)
                save_calculations(self.calculation_history)

                print("\n✅ Calculation completed successfully!")
                print(f"🧮 Answer : {total}\n")

                self.battery_manager.consume_battery(10)
                save_battery(self.battery_manager.battery)
                return


    # Method to calculate the multiplication of numbers
    def multiplication(self):
        while True:
            expression = input("✖️ Enter the multiplication expression:\n")

            if (not expression):
                print("\n❌ Expression cannot be empty.\n")
                return None

            elif (expression.startswith("*")):
                print("\n❌ Expression should not start with '*'.\n")
                return None

            elif (expression.endswith("*")):
                print("\n❌ Expression should not end with '*'.\n")
                return None

            elif ("**" in expression):
                print("\n❌ Expression should not contain '**'.\n")
                return None

            else:
                numbers = expression.split("*")

                # Validate user input
                for num in numbers:
                    if not num.isdigit():
                        print("\n❌ Expression should contain numbers only.\n")
                        return

                numbers = [int(num) for num in numbers]

                total = 1
                for number in numbers:
                    total = total * number

                # Save the operation in history
                calculator_record = {
                    "operation": "Multiplication",
                    "expression": expression,
                    "answer": total
                }

                self.calculator_history.append(calculator_record)
                save_calculations(self.calculation_history)

                print("\n✅ Calculation completed successfully!")
                print(f"🧮 Answer : {total}\n")

                self.battery_manager.consume_battery(2)
                save_battery(self.battery_manager.battery)
                return

    # Method to calculate the subtraction of numbers
    def subtraction(self):
        while True:
            expression = input("➖ Enter the subtraction expression:\n")

            if (not expression):
                print("\n❌ Expression cannot be empty.\n")
                return None

            elif (expression.startswith("-")):
                print("\n❌ Expression should not start with '-'.\n")
                return None

            elif (expression.endswith("-")):
                print("\n❌ Expression should not end with '-'.\n")
                return None

            elif ("--" in expression):
                print("\n❌ Expression should not contain '--'.\n")
                return None

            else:
                numbers = expression.split("-")

                # Validate user input
                for num in numbers:
                    if not num.isdigit():
                        print("\n❌ Expression should contain numbers only.\n")
                        return

                numbers = [int(num) for num in numbers]

                total = numbers[0]
                for j in range(1, len(numbers)):
                    total = total - numbers[j]

                print("\n✅ Calculation completed successfully!")
                print(f"🧮 Answer : {total}\n")

                self.battery_manager.consume_battery(2)
                save_battery(self.battery_manager.battery)

                # Save the operation in history
                calculator_record = {
                    "operation": "Subtraction",
                    "expression": expression,
                    "answer": total
                }

                self.calculator_history.append(calculator_record)
                save_calculations(self.calculation_history)
                return

    # Method to calculate the division of numbers
    def division(self):
        while True:
            num1 = input("➗ Enter the first number:\n")

            # Validate user input
            if (num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("\n❌ Number should contain digits only.\n")

        while True:
            num2 = input("➗ Enter the second number:\n")

            # Validate user input
            if (num2.isdigit()):
                num2 = int(num2)

                if (num2 != 0):
                    total = (num1 / num2)

                    print("\n✅ Calculation completed successfully!")
                    print(f"🧮 Answer : {total}\n")

                    expression = f"{num1}/{num2}"

                    # Save the operation in history
                    calculator_record = {
                        "operation": "Division",
                        "expression": expression,
                        "answer": total
                    }

                    self.calculator_history.append(calculator_record)
                    save_calculations(self.calculation_history)

                    self.battery_manager.consume_battery(2)
                    save_battery(self.battery_manager.battery)
                    return

                else:
                    print("\n❌ Error: Cannot divide by zero.\n")

            else:
                print("\n❌ Number should contain digits only.\n")


    # Method to find the remainder of numbers
    def modulus(self):
        while True:
            num1 = input("📊 Enter the first number:\n")

            # Validate user input
            if (num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("\n❌ Number should contain digits only.\n")

        while True:
            num2 = input("📊 Enter the second number:\n")

            # Validate user input
            if (num2.isdigit()):
                num2 = int(num2)

                if (num2 != 0):
                    total = (num1 % num2)

                    print("\n✅ Calculation completed successfully!")
                    print(f"🧮 Answer : {total}\n")

                    expression = f"{num1}%{num2}"

                    # Save the operation in history
                    calculator_record = {
                        "operation": "Modulus",
                        "expression": expression,
                        "answer": total
                    }

                    self.calculator_history.append(calculator_record)
                    save_calculations(self.calculation_history)

                    self.battery_manager.consume_battery(2)
                    return

                else:
                    print("\n❌ Error: Second number cannot be zero.\n")

            else:
                print("\n❌ Number should contain digits only.\n")


    # Method to find the square of a number
    def square(self):
        while True:
            number = input("🔲 Enter a number to find its square:\n")

            # Validate user input
            if (number.isdigit()):
                number = int(number)

                total = (number * number)

                print("\n✅ Calculation completed successfully!")
                print(f"🧮 Answer : {total}\n")

                expression = f"{number}*{number}"

                # Save the operation in history
                calculator_record = {
                    "operation": "Square",
                    "expression": expression,
                    "answer": total
                }

                self.calculator_history.append(calculator_record)
                save_calculations(self.calculation_history)

                self.battery_manager.consume_battery(2)
                return

            else:
                print("\n❌ Number should contain digits only.\n")

    # Method to find the cube of a number
    def cube(self):
        while True:
            number = input("🧊 Enter a number to find its cube:\n")

            # Validate user input
            if (number.isdigit()):
                number = int(number)

                total = (number * number * number)

                print("\n✅ Calculation completed successfully!")
                print(f"🧮 Answer : {total}\n")

                expression = f"{number}*{number}*{number}"

                # Save the operation in history
                calculator_record = {
                    "operation" : "Cube",
                    "expression" : expression,
                    "answer" : total
                }

                self.calculator_history.append(calculator_record)
                save_calculations(self.calculation_history)
                
                self.battery_manager.consume_battery(2)
                return

            else:
                print("\n❌ Number should contain digits only.\n")

    # Method to view the calculator history
    def view_calculator_history(self):
        print("\n" + "═"*14 + " 📜 CALCULATOR HISTORY " + "═"*14 + "\n")

        if (not self.calculator_history):
            print("╔════════════════════════════════════╗")
            print("║   📭 Calculator History is Empty   ║")
            print("╚════════════════════════════════════╝\n")

        else:
            # Display stored records
            for index, calculation in enumerate(self.calculator_history, start=1):
                print(f"🧮 Calculation #{index}")
                print(f"⚙️  Operation  : {calculation['operation']}")
                print(f"📝 Expression : {calculation['expression']}")
                print(f"✅ Answer     : {calculation['answer']}")
                print("─" * 35)

                self.battery_manager.consume_battery(1)

    # Method to clear the calculator history
    def clear_calculator_history(self):
        print("\n" + "═"*12 + " 🗑️ CLEAR CALCULATOR HISTORY " + "═"*12 + "\n")

        if (not self.calculator_history):
            print("╔════════════════════════════════════════════╗")
            print("║   📭 No Calculator History To Clear        ║")
            print("╚════════════════════════════════════════════╝\n")
            return

        else:
            while True:
                
                # Confirm before deleting all records
                sure_thing = input("⚠️  Are you sure? (y/n): ").lower()

                if (sure_thing == "y"):
                    self.calculator_history.clear()
                    save_calculations(self.calculation_history)

                    print("\n✅ Calculator history cleared successfully.\n")

                    self.battery_manager.consume_battery(2)
                    return

                elif (sure_thing == "n"):
                    return

                else:
                    print("\n❌ Please enter a valid choice (y/n).\n")

    # Method to take user choice for calculator
    def calculator_manager(self):
        if not self.battery_manager.check_battery():
            return

        self.see_calculator_menu()

        while True:
            print("\n" + "─"*42)
            print("🧮 What would you like to calculate?")
            print("─"*42)

            choice = input("\n➡️  Enter your choice: ")

            if choice.isdigit():
                choice = int(choice)

                if (choice == 1):
                    self.addition()
                elif (choice == 2):
                    self.subtraction()
                elif (choice == 3):
                    self.multiplication()
                elif (choice == 4):
                    self.division()
                elif (choice == 5):
                    self.modulus()
                elif (choice == 6):
                    self.square()
                elif (choice == 7):
                    self.cube()
                elif (choice == 8):
                    self.view_calculator_history()
                elif (choice == 9):
                    self.clear_calculator_history()
                elif (choice == 10):
                    self.see_calculator_menu()
                elif (choice == 11):
                    return
                else:
                    print("\n❌ Please enter a valid menu choice.\n")

            else:
                print("\n❌ Error: Choice must be a digit.\n")
