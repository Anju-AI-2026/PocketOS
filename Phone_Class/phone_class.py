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
        print("6.Show phone battery")
        print("7.Charge battery")
        print("8.See menu")
        print("9.Add Contact")
        print("10.View saved contact")
        print("11.Delete contact")
        print("12.Search contact") 
        print("13.View message history") 
        print("14.Delete message")
        print("15.Exit") 

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
            if (name in self.contact):
                print("Contact already exit")
                return
            else:
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
            print("==========CONTACT BOOK==========")
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
            while True:
                contact_name = input("Enter the contact name to delete :")
                if (contact_name.isalnum()):
                    if (contact_name in self.contact):
                        del self.contact[contact_name]
                        print("Contact deleted successfully!")
                        break 
                else:
                    print("Contact not found")         

    # Method to search for contact in recent call and contact also
    def search_contact(self):
        search_record = input("Enter the name or number to search :") 
        found = False
        if (search_record.isdigit()):
            for key,value in self.contact.items():
                if (search_record == value):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :{key}")
                    print(f"Number : {value}")
                    print("="*20)
                    return
            for call in self.call_list:
                if (search_record == call["number"]):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :",call["name"])
                    print(f"Number :",call["number"])
                    print("="*20)
                    return

        else:
            for key, value in self.contact.items():
                if (search_record == key):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :{search_record}")                        
                    print(f"Number : {self.contact[search_record]}")
                    print("="*20)
                    return 
            for call in self.call_list:
                if (search_record == call["name"]) :
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :",call["name"])
                    print(f"Number :",call["number"])
                    print("="*20)
                    return

        if not found:
            print("====================")
            print("Contact not found")
            print("====================")
        


    # Method to make a phone call and store call history
    def call(self):
        user_choice=(input("Enter the contact number or name:")) 
        if (user_choice.isdigit()):   
            if (len(user_choice)==10):
                    for key,value in self.contact.items():
                        if (value == user_choice):
                            print(f"Calling {key}")
                            print("Dialing!!!!!")
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
                                            print("Dialing!!!")
                                            return 
                                    else:
                                        print("Name only contain alphabet or alphanumeric name")       
                            elif (save_choice == "n"):
                                print("Calling unknown number")
                                print("Dialing!!!!!")  
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
                print("Dialing!!!!!")
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

#feat: add message history viewing and deletion
 # Method to display call history
    def view_message_history(self):
        self.battery = self.battery - 2

        if not self.message_list:
            print("==========================")
            print("No message history available.")
            print("==========================")
            return

        print("\n========== MESSAGE HISTORY ==========\n")

        for index, message in enumerate(self.message_list, start=1):
            print(f"Message {index}")
            print(f"Name   : {message['name']}")
            print(f"Number : {message['number']}")
            print(f"Messgae : {message['message']}")
            print(f"Type   : {message['type']}")
            print("-" * 35)

    def delete_message(self):
        self.battery=self.battery-2
        if (not self.message_list):
            print("Message history is empty")
        else:
            while True:
                contact_name = input("Enter the contact name to delete :")
                if (contact_name.isalnum()):
                    for i, message in enumerate(self.message_list):
                        if contact_name == message["name"]:
                            del self.message_list[i]
                            print("Message deleted successfully!")
                            return
            else:
                print("Message not found") 


    # Method to send messages and store message history
    def message(self):
        user_choice=(input("Enter the phone number or name to send message : "))
        if (user_choice.isdigit()):
            if (len(user_choice)==10):
                for key,value in self.contact.items():
                    if (value == user_choice):
                        msg=input(f"Enter the message to send {key} : ")    
                        message_chat={
                            "name" : key,
                            "number" : value,
                            "message" : msg,
                            "type" : "Sent"
                        }
                        print("Message sent!!!")
                        self.message_list.append(message_chat)
                        self.battery=self.battery-5
                        return
                while True:
                    save_choice=input("Do you want to save the number? (y/n) :").lower()
                    if (save_choice.isalpha()):
                        if save_choice == "y":
                    
                            while True:
                                name = input("Enter the name to save contact :")
                                if (name.replace(" ","").isalnum()):
                                    if(name.isdigit()):
                                        print("Name should not be only made up of number :")
                                    else:
                                        msg=input("Enter the message to send :")
                                        message_chat={
                                            "name" : name,
                                            "number" : user_choice,
                                            "message" : msg,
                                            "type" : "Sent"
                                        }  
                                        print("Message sent!!!")
                                        self.message_list.append(message_chat) 
                                        self.contact[name] = user_choice
                                        self.battery=self.battery-5
                                        return
                                else:
                                    print("Name only contain alphanumeric ")    
                        elif (save_choice == "n"):
                            msg=input("Enter the message to send unknown number :")
                            message_chat= {
                                "name" : "Unknown",
                                "number" : user_choice,
                                "message" : msg,
                                "type" : "Sent"
                            }  
                            print("Message sent!!!")
                            self.message_list.append(message_chat) 
                            self.battery=self.battery-5
                            return
                        else:
                            print("Please enter a valid choice!")
                    else:
                        print("Please enter a valid choice!")        
        else:
            if(user_choice in self.contact):
                msg=input(f"Enter the message to send {user_choice}: ")
                message_chat= {
                    "name" : user_choice,
                    "number" : self.contact[user_choice],
                    "message" : msg,
                    "type" : "Sent"
                }  
                print("Message sent!!!")
                self.message_list.append(message_chat) 
                self.battery=self.battery-5
                return
            else:
                print("Contact not found") 

    # Method to play music and reduce battery percentage
    def playmusic(self):
        music=input("Enter the song name : ")
        print("Plyaing",music,"music") 
        self.battery=self.battery-15

     
     # Method to calculate total sum of numbers    
     def addition(self):
        numbers = []
        while True :
            num = input("Enter the limit to the numbers:")
            if (num.isdigit()):
                num = int(num)
                for i in range(1,num+1):
                    while True:
                        x=input(f"Enter the {i} numbers:")
                        if (x.isdigit()):
                            x = int(x)
                            numbers.append(x)
                            break
                        else:
                            print("Invalid input!! Enter again")     
                total = sum(numbers)
                print("The sum of all number is :",total)
                return
            else:
                print("The limit should be a number.")
                 
     # Method to calculate the multiplication of numbers
     def multiplication(self):
        numbers = []
        total = 1
        while True :
            num = input ("Enter the limit to the numbers :")
            if (num.isdigit()):
                num = int(num)
                for i in range(1,num+1):
                    while True:
                        x = input(f"Enter the {i} numbers :")
                        if (x.isdigit()):
                            x = int(x)
                            numbers.append(x)
                            break
                        else:
                            print("Invalid Input!! Enter again")
                for number in numbers:
                    total = total * number          
                print("The multiplication of all number is :",total)
                return
            else:
                print("The limit should be a number") 

      def subtraction(self):
        while True:
            numbers = []
            while True :
                num = input("Enter the limit to the numbers :")
                if(num.isdigit()):
                    num = int(num)
                    for i in range(1,num+1):
                        while True:
                            x = input(f"Enter the {i} numbers :")
                            if (x.isdigit()):
                                x = int(x)
                                numbers.append(x)
                                break
                            else:
                                print("Invalid Input!! Enter again")
                total = numbers[0]                
                for j in range (1,len(numbers)):
                    total = total - numbers[j]
                print("The subtraction of numbers is :", total)     
                return
            else:
                print("The limit should be a number") 

     # Method to calculate the division
     def division(self):
        while True:
            num1=input("Enter the first number :")
            if(num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("Number should be a digit")
        while True:
            num2 = input("Enter the second number :")
            if(num2.isdigit()):
                num2=int(num2)
                if (num2 != 0):
                    print("The division of numbers is :" ,(num1 / num2) )
                    return
                else:
                    print("Error : Cannot divide by zero.")
            else:
                print("Number should be a digit")
