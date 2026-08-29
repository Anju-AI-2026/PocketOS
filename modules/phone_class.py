# Importing all manager modules for the Phone Management System

from modules.contacts import ContactManager
from modules.calls import CallManager
from modules.messages import MessageManager
from modules.calculator import CalculatorManager
from modules.games import GameManager
from modules.battery import BatteryManager
from modules.music import MusicManager
from modules.settings import SettingsManager
from modules.storage import load_password
import os

# Program to demonstrate a Phone class using multiple inheritance
# Main Phone class that combines all phone applications

class Phone(ContactManager,
            CallManager,
            MessageManager,
            CalculatorManager,
            GameManager,
            MusicManager,
            SettingsManager
            ):

    # Constructor to initialize phone details and manager classes
    def __init__(self):

        self.real_password = load_password()

        self.battery_manager = BatteryManager()
        CalculatorManager.__init__(self, self.battery_manager)
        ContactManager.__init__(self, self.battery_manager)
        CallManager.__init__(self, self.battery_manager)
        MessageManager.__init__(self, self.battery_manager)
        MusicManager.__init__(self, self.battery_manager)
        SettingsManager.__init__(self, self.battery_manager)

    # Method to display the main application menu
    def see_menu(self):
        self.battery_manager.show_status()
        print("╔" + "═"*54 + "╗")
        print("║                  📱 MAIN MENU                        ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. 📇 Contacts                                      ║")
        print("║  2. 📞 Calls                                         ║")
        print("║  3. 💬 Messages                                      ║")
        print("║  4. 🎵 Music Player                                  ║")
        print("║  5. 🧮 Calculator                                    ║")
        print("║  6. 🎮 Games                                         ║")
        print("║  7. 🔋 Battery Manager                               ║")
        print("║  8. ⚙️  Settings                                      ║")
        print("║  9.🚪 Exit                                           ║")
        print("╚" + "═"*54 + "╝")

    # Method to clear the terminal screen for a new page view
    def clear_screen(self):
        os.system("cls")   

# Main interface of the Phone Management System
print("╔" + "═"*68 + "╗")
print("║                   📱 PHONE MANAGEMENT SYSTEM                       ║")
print("╚" + "═"*68 + "╝")

print()
print("             ╔══════════════════════════════════════╗")
print("             ║       🔐 PASSWORD AUTHENTICATION     ║")
print("             ╚══════════════════════════════════════╝")

# Creating a Phone object
phone1 = Phone()

# Calling the password authentication function
phone1.authenticate_password()

input("⏩ Press Enter to continue...")

# Displaying the menu until the user exits the program
phone1.see_menu()

print("\n" + "─"*45)
print("📱 Which application would you like to open?")
print("─"*45)

while True:

    if not phone1.battery_manager.check_battery():
        break

    choice = input("\n➡️  Enter your choice: ")
    print()

    if (choice.isdigit()):

        choice = int(choice)

        if choice == 1:
            phone1.clear_screen()
            phone1.contact_manager()
            phone1.see_menu()

        elif choice == 2:
            phone1.clear_screen()
            phone1.call_manager()
            phone1.see_menu()

        elif choice == 3:
            phone1.clear_screen()
            phone1.message_manager()
            phone1.see_menu()

        elif choice == 4:
            phone1.clear_screen()
            phone1.music_manager()
            phone1.see_menu()

        elif choice == 5:
            phone1.clear_screen()
            phone1.calculator_manager()
            phone1.see_menu()

        elif choice == 6:
            phone1.clear_screen()
            phone1.game_manager()
            phone1.see_menu()

        elif choice == 7:
            phone1.clear_screen()
            if not phone1.battery_manager.battery_manager():
                break

        elif choice == 8:
            phone1.clear_screen()
            phone1.settings_manager()
            phone1.see_menu()    
            
        elif choice == 9:
            exit()

        else:
            print("\n❌ Invalid choice!")
            print("Please enter a number between 1 and 9.\n")

    else:
        print("\n❌ Error: Choice must be a digit.\n")
                    
    
        