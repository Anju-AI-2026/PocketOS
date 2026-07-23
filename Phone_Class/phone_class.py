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

# Password authentication before accessing the phone
real_p=12345   

while True:
    
    password=input("\nEnter the password 🗝️  : ")

    if (password.isdigit()):
        password = int(password)
        if(real_p==password):
            print("\n✅ Access Granted!")
            break
        else:
            print("\n❌Incorrect password")
    else:
        print("\nThe password should contain digits only")

input("\nPress Enter to Continue...")

# Taking phone details from the user
name=input("Enter the phone company name : ")
brand=input("Enter the mobile phone brand name : ")
colour=input("Enter the mobile phone colour : ")
memory=input("Enter the memory of the mobile phone : ")

# Creating a Phone object
phone1=Phone(name,brand,colour,memory)

# Displaying menu repeatedly until the user exits the program
phone1.see_menu()

# Processing user's menu choice
while True:

    choice=int(input("Enter a choice number from the menu : "))

    if not phone1.battery_manager.check_battery():
        continue
    if choice==1:
        phone1.showdetails()
    elif choice==2:
        phone1.contact_manager()
    elif choice==3:
        phone1.call_manager()
    elif choice==4:
        phone1.message_manager()
    elif choice==5:
        phone1.music_manager() 
    elif choice==6:
        phone1.calculator_manager()
    elif choice==7:
        phone1.game_manager()
    elif choice == 8:
        phone1.battery_manager.show_battery()
    elif choice == 9:
        phone1.battery_manager.battery_manager()
    elif choice == 11:
        exit()
    else:
        print("Please enter a valid number!!!")                    



