class ContactManager:

    def __init__(self):
        self.contacts = {}

    # Method to see the contact menu
    def see_contact_menu(self):
        print("="*35)
        print("            CONTACT MENU ")
        print("="*35)
        print("1.Add contacts")
        print("2.View contacts")
        print("3.Delete contacts")
        print("4.Search contact")
        print("5.Clear contacts")
        print("6.See menu")
        print("7.Back")

    # Adds a contact after validating the name and phone number
    def add_contact(self):
        self.battery=self.battery-2
        while True:
            name=input("Enter the contact name :")
            if (name in self.contacts):
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
                    self.contacts[name] = phone_number
                    print("Phone number successfully saved")
                    break
                else:
                    print("Phone number should not contain charector!!")
            else:
                print("Phone number should contain 10 digit")  

    # Displays all contacts stored in the contact book
    def view_contact(self):
        self.battery=self.battery-2
        if (not self.contacts):
            print("=================")
            print("Contact is empty")
            print("=================")
        else:
            print()
            print("==========CONTACT BOOK==========")
            print()
            print("\nContacts :")
            count = 1
            for key,value in self.contacts.items():
                    print(count)
                    print("Name :",key)
                    print("Number :",value) 
                    print("-" * 20)  
                    count=count+1

        # Method to delete the contact from the contact
    def delete_contact(self):
        self.battery=self.battery-2
        if (not self.contacts):
            print("Contact is empty")
        else:
            while True:
                contact_name = input("Enter the contact name to delete :")
                if (contact_name.isalnum()):
                    if (contact_name in self.contacts):
                        del self.contacts[contact_name]
                        print("Contact deleted successfully!")
                        break 
                    else:
                        print("Contact not found")         

    # Method to search for contact in recent call and contact also
    def search_contact(self):
        search_record = input("Enter the name or number to search :") 
        found = False
        if (search_record.isdigit()):
            for key,value in self.contacts.items():
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
            for key, value in self.contacts.items():
                if (search_record == key):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :{search_record}")                        
                    print(f"Number : {self.contacts[search_record]}")
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

    # Method to create the clear the contact 
    def clear_contact(self):
        if (not self.contacts):
            print("Contact is empty can not clear")
            return
        else:
            while True:
                sure_thing = input("Are you sure (y/n) :").lower()
                if (sure_thing == "y"):
                    self.contacts.clear()
                    print("Contacts deleted sucssessfully")
                    return
                elif (sure_thing == "n"):
                    return
                else:
                    print("Enter a valid choice")                         

    def contact_manager(self):
        if (self.battery <= 20):
            print("Battery getting low!! Please charge it.")
            return
        self.see_contact_menu()

        while True :
            choice = input("Enter a choice from the menu :")
            if (choice.isdigit()):
                choice = int(choice)
                
                if choice == 1 :
                    self.add_contact()
                elif choice == 2 :
                    self.view_contact()
                elif choice == 3 :
                    self.delete_contact()
                elif choice == 4 :
                    self.search_contact()
                elif choice == 5 :
                    self.clear_contact()
                elif choice == 6 :
                    self.see_menu()
                elif choice == 7 :
                    return
                else:
                    print("Enter a valid choice")
            else:
                print("Error : Choice should be a digit") 
