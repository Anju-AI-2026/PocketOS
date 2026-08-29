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

                    
    
        