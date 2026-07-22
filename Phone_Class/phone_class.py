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
    def __init__(self,name,brand,colour,memory):

        CalculatorManager.__init__(self, self.battery_manager)
        ContactManager.__init__(self, self.battery_manager)
        CallManager.__init__(self, self.battery_manager)
        MessageManager.__init__(self, self.battery_manager)
        MusicManager.__init__(self, self.battery_manager)
        self.battery_manager = BatteryManager()

        self.name=name
        self.brand=brand
        self.colour=colour
        self.memory=memory

    # Method to display phone details
    def showdetails(self):
        self.battery=self.battery-2
        print("Mobile Phone company name :",self.name)
        print("The mobile phone brand i : ",self.brand)
        print("The colour of the mobile phone",self.colour)
        print("The memory of the mobile phone is : ",self.memory)

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






