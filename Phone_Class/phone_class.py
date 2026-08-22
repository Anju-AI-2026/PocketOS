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

    # Method to display the main application menu
    def see_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                  📱 MAIN MENU                        ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. 📇 Contacts                                      ║")
        print("║  2. 📞 Calls                                         ║")
        print("║  3. 💬 Messages                                      ║")
        print("║  4. 🎵 Music Player                                  ║")
        print("║  5. 🧮 Calculator                                    ║")
        print("║  6. 🎮 Games                                         ║")
        print("║  7. 🔋  Battery Manager                              ║")
        print("║  8.🚪 Exit                                          ║")
        print("╚" + "═"*54 + "╝")

    # Method to clear the terminal screen for a new page view
    def clear_screen(self):
        os.system("cls")   
