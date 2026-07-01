# Program to demonstrate a phone class 

class Phone:

     # Constructor to initialize phone details and default values
    def __init__(self,name,brand,colour,memory):
        self.name=name
        self.brand=brand
        self.colour=colour
        self.memory=memory
        self.call_list=[]
        self.message_list=[]
        self.contact={}
        self.battery=100

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
        print("2.Make a call")
        print("3.Send a message")
        print("4.Play a music")
        print("5.Show call history")
        print("6.Show message history")
        print("7.Show phone battery")
        print("8.Charge battery")
        print("9.See menu")
        print("10.Add Contact")
        print("11.View saved contact")
        print("12.Delete contact")
        print("13.Exit")  

    # Method to recharge the battery
    def charge_phone(self):
        if (self.battery == 100):
            print("Battery is already full !!")
            return
        if (self.battery < 100):
            charge = int(input("Enter the battery parcentage to charge below 100 :"))
            if (charge > 100):
                print("Please enter battery below 100")    
            else:
                print("Current battery :",self.battery)
                print("Charge amount :", charge)
                self.battery = self.battery+charge   
                if (self.battery > 100):
                    self.battery = 100 
                print("\nBattery charged successfully.")
                print("Current battery :", self.battery)   

    # Adds a contact after validating the name and phone number
    def add_contact(self):
        self.battery=self.battery-2
        while True:
            name=input("Enter the contact name :")
            if (name.replace(" ","").isalnum()):
                if (name.isdigit()):
                    print("Contact name should not be only made up of numbers!")
                else:
                    break
            else:
                print("Name only contain alphabet or alphanumeric name")

        while True:
            phone_number=input("Enter phone number :")
            if (len(phone_number) == 10):
                if (phone_number.isdigit()):
                    self.contact[name] = phone_number
                    print("Phone number successfully saved")
                    break
                else:
                    print("Phone number should not contain charector!!")
            else:
                print("Phone number should contain 10 digit")  

   # Displays all contacts stored in the contact book
    def view_contact(self):
        self.battery=self.battery-2
        if (not self.contact):
            print("=================")
            print("Contact is empty")
            print("=================")
        else:
            print()
            print("==========CALL HISTORY==========")
            print()
            print("\nContacts :")
            count = 1
            for key,value in self.contact.items():
                    print(count)
                    print("Name :",key)
                    print("Number :",value) 
                    print("-" * 20)  
                    count=count+1

    # Method to display call history
    def view_call_history(self):
        self.battery = self.battery - 2

        if not self.call_list:
            print("==========================")
            print("No call history available.")
            print("==========================")
            return

        print("\n========== CALL HISTORY ==========\n")

        for index, call in enumerate(self.call_list, start=1):
            print(f"Call {index}")
            print(f"Name   : {call['name']}")
            print(f"Number : {call['number']}")
            print(f"Type   : {call['type']}")
            print("-" * 35)

    # Method to delete the contact from the contact
    def delete_contact(self):
        self.battery=self.battery-2
        if (not self.contact):
            print("Contact is empty")
        else:
            contact_name = input("Enter the contact name to delete :")
            if (contact_name in self.contact):
                del self.contact[contact_name]
                print("Contact deleted successfully!")
            else:
                print("Contact not found!!")                                  

  # Method to make a phone call and store call history
    def call(self):
        user_choice=(input("Enter the contact name or phone number :")) 
        if (user_choice.isdigit()):   
            if (len(user_choice)==10):
                    for key,value in self.contact.items():
                        if (value == user_choice):
                            print(f"Calling {key}")
                            print("Dailing!!!!!")
                            call_record = {
                                "name" : key ,
                                "number" : value,
                                "type" : "Outgoing" 
                            }
                            self.call_list.append(call_record)
                            self.battery=self.battery-10
                            return
                    while True:
                        save_choice = input("Do you want to save the number? (y/n) :").lower()
                        if (save_choice.isalpha()):
                            if save_choice == "y":
                                while True:
                                    name=input("Enter the contact name :")
                                    if (name.replace(" ","").isalnum()):
                                        if (name.isdigit()):
                                            print("Contact name should not be only made up of numbers!")
                                        else:
                                            call_record = {
                                                "name" : name,
                                                "number" : user_choice,
                                                "type" : "Outgoing"
                                            }
                                            self.call_list.append(call_record)
                                            self.contact[name] = user_choice
                                            self.battery=self.battery-10
                                            print("Contact saved successfully!")
                                            print(f"Calling {name}")
                                            print("Dailing!!!")
                                            return 
                                    else:
                                        print("Name only contain alphabet or alphanumeric name")       
                            elif (save_choice == "n"):
                                print("Calling unknown number")
                                print("Dailing!!!!!")  
                                call_record = {
                                    "name" : "Unknown",
                                    "number" : user_choice,
                                    "type" : "Outgoing"
                                }
                                self.call_list.append(call_record)
                                self.battery=self.battery-10
                                return
                            else:
                                print("Please enter a valid choice!")
                        else:
                            print("Please enter a valid choice")
            else:   
                print("Please enter a 10 digit number")
        else:
            if (user_choice in self.contact):
                print(f"Calling {user_choice}")
                print("Dailing!!!!!")
                call_record={
                    "name" : user_choice,
                    "number" : self.contact[user_choice],
                    "type" : "Outgoing" 
                }
                self.call_list.append(call_record)
                self.battery=self.battery-10
                return
            else:
                print("Contact not found")

    # Method to send messages and store message history
    def message(self):
        user_choice=(input("Enter the phone number or name to send message : "))
        if (user_choice.isdigit()):
            if (len(user_choice)==10):
                for key,value in self.contact.items():
                    if (value == user_choice):
                        msg=input(f"Enter the message to send {key} : ")    
                        print("Message sent!!!")
                        self.message_list.append((user_choice,msg))
                        self.battery=self.battery-5
                        return
                msg=input("Enter the message to send unknown number :")
                print("Message sent!!!")
                self.message_list.append((user_choice,msg))
                self.battery=self.battery-5   
                return
            else:
                print("Please enter the correct contact number")
                return
        else:
            if(user_choice in self.contact):
                msg=input(f"Enter the message to send {user_choice}: ")
                print("Message sent!!!")
                self.message_list.append((self.contact[user_choice],msg))
                self.battery=self.battery-5
                return
            else:
                 print("Contact not found")
         

    # Method to play music and reduce battery percentage
    def playmusic(self):
        music=input("Enter the song name : ")
        print("Plyaing",music,"music") 
        self.battery=self.battery-15
         




