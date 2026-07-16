class MessageManager:

    def __init__(self):
        self.message_list=[]

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
