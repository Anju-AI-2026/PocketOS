# Importing all manager modules for the Phone Management System

from contacts import ContactManager
from calls import CallManager
from messages import MessageManager
from calculator import CalculatorManager
from games import GameManager
from battery import BatteryManager
from music import MusicManager
from settings import SettingsManager
from storage import load_password
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

        self.battery_manager = BatteryManager()
        CalculatorManager.__init__(self, self.battery_manager)
        ContactManager.__init__(self, self.battery_manager)
        CallManager.__init__(self, self.battery_manager)
        MessageManager.__init__(self, self.battery_manager)
        MusicManager.__init__(self, self.battery_manager)
        SettingsManager.__init__(self, self.battery_manager)

        self.name = "Samsung"
        self.brand = "Galaxy S24"
        self.colour = "Black"
        self.memory = "256 GB"

    # Method to display phone information
    def showdetails(self):
        self.battery_manager.consume_battery(2)

        print("╔" + "═"*54 + "╗")
        print("║                📱 PHONE INFORMATION                  ║")
        print("╠" + "═"*54 + "╣")
        print(f"║  🏢 Company : {self.name:<37}  ║")
        print(f"║  📱 Model   : {self.brand:<37}  ║")
        print(f"║  🎨 Colour  : {self.colour:<37}  ║")
        print(f"║  💾 Storage : {self.memory:<37}  ║")
        print("╚" + "═"*54 + "╝")

    # Method to display the main application menu
    def see_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                  📱 MAIN MENU                        ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. 📄 Phone Details                                 ║")
        print("║  2. 📇 Contacts                                      ║")
        print("║  3. 📞 Calls                                         ║")
        print("║  4. 💬 Messages                                      ║")
        print("║  5. 🎵 Music Player                                  ║")
        print("║  6. 🧮 Calculator                                    ║")
        print("║  7. 🎮 Games                                         ║")
        print("║  8. 🔋 Battery Status                                ║")
        print("║  9. ⚙️  Battery Manager                               ║")
        print("║ 10. 🚪 Exit                                          ║")
        print("╚" + "═"*54 + "╝")

    # Method to clear the terminal screen for a new page view
    def clear_screen(self):
        os.system("cls")   
