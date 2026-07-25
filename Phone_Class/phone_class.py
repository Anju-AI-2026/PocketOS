from contacts import ContactManager
from calls import CallManager
from messages import MessageManager
from calculator import CalculatorManager
from games import GameManager
from battery import BatteryManager
from music import MusicManager

# Program to demonstrate a phone class 

class Phone(ContactManager, 
            CallManager, 
            MessageManager, 
            CalculatorManager, 
            GameManager, 
            MusicManager
            ):

     # Constructor to initialize phone details and default values
    def __init__(self,):

        CalculatorManager.__init__(self, self.battery_manager)
        ContactManager.__init__(self, self.battery_manager)
        CallManager.__init__(self, self.battery_manager)
        MessageManager.__init__(self, self.battery_manager)
        MusicManager.__init__(self, self.battery_manager)
        self.battery_manager = BatteryManager()

        self.name = "Samsung"
        self.brand = "Galaxy S24"
        self.colour = "Black"
        self.memory = "256 GB"

    # Method to display phone details
    def showdetails(self):
        self.battery_manager.consume_battery(2)
        print("╔" + "═"*54 + "╗\n")
        print("                 📱 SAMSUNG GALAXY S24\n")
        print("╠" + "═"*54 + "╣\n")

        print(f"   🏢 Company    : {self.name}")
        print(f"   📱 Model      : {self.brand}")
        print(f"   🎨 Colour     : {self.colour}")
        print(f"   💾 Storage    : {self.memory}\n")

        print("╚" + "═"*54 + "╝")

    # Method to see the menu
    def see_menu(self):
        print("========Menu========")
        print("1.Show the details of the Mobile phone")
        print("2.Contact App")
        print("3.Message App")
        print("4.Call App")
        print("5.Music app")
        print("6.Calculator")
        print("7.Game app")
        print("8..Show phone battery")
        print("9.Charge battery")
        print("10.See menu")
        print("11.Exit") 
