# Class to demonstrate the contact methods
class ContactManager:

    def __init__(self):
        self.contacts = {}


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
