class CallManager:

    def __init__(self):
        self.call_list=[]

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
                                            self.contacts[name] = user_choice
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
            if (user_choice in self.contacts):
                print(f"Calling {user_choice}")
                print("Dialing!!!!!")
                call_record={
                    "name" : user_choice,
                    "number" : self.contacts[user_choice],
                    "type" : "Outgoing" 
                }
                self.call_list.append(call_record)
                self.battery=self.battery-10
                return
            else:
                print("Contact not found")    
