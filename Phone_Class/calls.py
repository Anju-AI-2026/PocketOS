class CallManager:

    def __init__(self, battery_manager):
        self.battery_manager = battery_manager
        self.call_list=[]

    # Method to create the call menu
    def see_call_menu(self):
        print("="*35)
        print("            CALL MENU")
        print("="*35)
        print("1.Make a call")    
        print("2.View call history")
        print("3.Delete call history")
        print("4.Clear call history")
        print("5.See menu")
        print("6.Back")

    # Method to make a phone call and store call history
    def call(self):
        user_choice=(input("Enter the contact number or name:")) 
        if (user_choice.isdigit()):   
            if (len(user_choice)==10):
                    for key,value in self.contacts.items():
                        if (value == user_choice):
                            print(f"Calling {key}")
                            print("Dialing!!!!!")
                            call_record = {
                                "name" : key ,
                                "number" : value,
                                "type" : "Outgoing" 
                            }
                            self.call_list.append(call_record)
                            self.battery_manager.consume_battery(5)
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
                                            self.contacts[name] = user_choice
                                            self.battery=self.battery-10
                                            print("Contact saved successfully!")
                                            print(f"Calling {name}")
                                            print("Dialing!!!")
                                            self.battery_manager.consume_battery(5)
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
                                self.battery_manager.consume_battery(5)
                                return
                            else:
                                print("Please enter a valid choice!")
                        else:
                            print("Please enter a valid choice")
            else:   
                print("Please enter a 10 digit number")
        else:
            if (user_choice in self.contacts):
                print(f"Calling {user_choice}")
                print("Dialing!!!!!")
                call_record={
                    "name" : user_choice,
                    "number" : self.contacts[user_choice],
                    "type" : "Outgoing" 
                }
                self.call_list.append(call_record)
                self.battery_manager.consume_battery(5)
                return
            else:
                print("Contact not found")    

    # Method to display call history
    def view_call_history(self):
        self.battery_manager.consume_battery(2)

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

    # Method to delete a call history
    def delete_call_history(self):
        if (not self.call_list):
            print("The call history is empty can not delete")
            return
        else:
            for index, call in enumerate(self.call_list, start=1):
                print(f"Call {index}")
                print(f"Name   : {call['name']}")
                print(f"Number : {call['number']}")
                print(f"Type   : {call['type']}")
                print("-" * 35) 
            while True:
                choice = input("Enter the call number to delete::")
                if (choice.isdigit()):
                    choice = int(choice) 
                    length = len(self.call_list)
                    if (choice >= 1 and choice <= length):
                        del self.call_list[choice-1]
                        self.battery_manager.consume_battery(2)
                        return
                    else:
                        print("Choice is out of range")
                        
    # Method to clear the call history
    def clear_call_history(self):
        if (not self.call_list):
            print("The call history is empty can not delete")
            return
        else:
            while True:
                sure_thing = input("Are you sure (y/n) :").lower()
                if (sure_thing == "y"):
                    self.call_list.clear()
                    print("Call history deleted sussessfully")
                    self.battery_manager.consume_battery(2)
                    return
                elif (sure_thing == "n"):
                    return
                else:
                    print("Enter a valid choice")    

    # Method to create the contact controller
    def call_manager(self):
        if not self.battery_manager.check_battery():
            return
        self.see_call_menu()
        while True :
            choice = input("Enter the choice from above menu :")
            if choice.isdigit():
                if choice == 1 :
                    self.call()
                elif choice == 2 :
                    self.view_call_history()
                elif choice == 3 :
                    self.delete_call_history()
                elif choice == 4 :
                    self.clear_call_history()
                elif choice == 5 :
                    self.see_call_menu()    
                elif choice == 6 :
                    return
                else:
                    print("Enter a valid choice ")
            else:
                print("Error : choice should be a digit")      
