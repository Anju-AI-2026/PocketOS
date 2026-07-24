class MessageManager:

    def __init__(self, battery_manager):
        self.battery_manager = battery_manager
        self.message_list=[]

    # Method to see the message menu
    def see_message_menu(self):
        print("="*35)
        print("            MESSAGE MENU")
        print("="*35)
        print("1.Send a message")
        print("2.View message history")
        print("3.Delete message ")
        print("4.Clear message history")
        print("5.See menu")
        print("6.Back")    

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
                        self.battery_manager.consume_battery(5)
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
                                        self.battery_manager.consume_battery(5)
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
                            self.battery_manager.consume_battery(5)
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
                self.battery_manager.consume_battery(5)
                return
            else:
                print("Contact not found")    

    # Method to display call history
    def view_message_history(self):
        self.battery_manager.consume_battery(2)

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

    # Method to delete a individual message from history
    def delete_message(self):
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
                            self.battery_manager.consume_battery(2)
                            return
                    print("Contact not found")    
                else:
                    print("Name should be alphanumeric only")     

    # Method to clear the message history
    def clear_message_history(self):
        if (not self.message_list):
            print("Message history is empty. Nothing to clear.")
            return
        else:
            while True:
                sure_thing = input("Are you sure (y/n) :").lower()
                if (sure_thing == "y"):
                    self.message_list.clear()
                    print("Message history deleted sussessfully")
                    self.battery_manager.consume_battery(2)
                    return
                elif (sure_thing == "n"):
                    return
                else:
                    print("Enter a valid choice")                        

    # Method to create the message controller
    def message_manager(self):
        if not self.battery_manager.check_battery():
            return
        self.see_message_menu()  
        while True :
            choice = input("Enter a choice from above menu :")
            if choice.isdigit():
                choice = int(choice)
                if choice == 1 :
                    self.message()
                elif choice == 2 :
                    self.view_message_history()
                elif choice == 3 :
                    self.delete_message()
                elif choice == 4 :
                    self.clear_message_history()
                elif choice == 5 :
                    self.see_message_menu()
                elif choice == 6 :
                    return
                else:
                    print("Enter a valid choice")
            else:
                print("Error : Choice should be a digit")                       
