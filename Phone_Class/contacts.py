class ContactManager:

    def __init__(self, battery_manager):
        self.battery_manager = battery_manager
        self.contacts = {}

    # Method to see the contact menu
    def see_contact_menu(self):
        print("╔" + "═"*54 + "╗\n")
        print("                 📇 CONTACT MANAGER\n")
        print("╠" + "═"*54 + "╣\n")
        print("1.➕  Add contacts\n")
        print("2.👀  View contacts\n")
        print("3.🗑️  Delete contacts\n")
        print("4.🔍  Search contact\n")
        print("5.🧹  Clear contacts\n")
        print("6.📋  See menu\n")
        print("7.🔙  Back")
        print("╚" + "═"*54 + "╝\n")

    # Adds a contact after validating the name and phone number
    def add_contact(self):
        print("\n=================➕ADD CONTACT=================")
        self.battery_manager.consume_battery(2)
        while True:
            print("")
            name=input("Enter the contact name :\n")
            if (name in self.contacts):
                print("\n======================")
                print("Contact already exit\n")
                print("======================\n")
                return
            else:
                if (name.replace(" ","").isalnum()):
                    if (name.isdigit()):
                        print("\n")
                        print("\n❌ Invalid Input")  
                        print("Contact name should not be only made up of numbers!\n")
                    else:
                        break
                else:
                    print("\n❌ Invalid Input")  
                    print("Name only contain alphabet or alphanumeric name\n")

        while True:
            phone_number=input("\nEnter phone number :\n")
            if phone_number.isdigit():
                if (len(phone_number) == 10):
                    if phone_number in self.contacts.values() :
                        print("The phone number already exits")
                    else:
                        self.contacts[name] = phone_number
                        print("✅ Contact added successfully!")
                        print("=====================================")
                        self.battery_manager.consume_battery(2)
                        break
                else:
                    print("Phone number should contain 10 digit")  
            else:
                print("The phone number should be numbers")        

    # Displays all contacts stored in the contact book
    def view_contact(self):
        print("\n==================👀 VIEW CONTACT==================")

        self.battery_manager.consume_battery(2)
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
        print("\n" + "═" * 16 + " 🗑️ DELETE CONTACT " + "═" * 16)
        self.battery_manager.consume_battery(2)

        if (not self.contacts):
            print("\n📭 Contact book is empty.\n")
        else:
            while True:
                print("\n" + "─" * 45)
                contact_name = input("👤 Enter the contact name to delete:\n")
                print("─" * 45)

                if contact_name.replace(" ", "").isalnum():
                    if (contact_name in self.contacts):
                        del self.contacts[contact_name]
                        print("\n✅ Contact deleted successfully!\n")
                        self.battery_manager.consume_battery(2)
                        break
                    else:
                        print("\n❌ Contact not found.")
                else:
                    print("\n❌ Invalid input.")
                    print("Name can contain only letters or alphanumeric characters.\n")

    # Method to search for contact in recent call and contact also
    def search_contact(self):
        print("\n" + "═" * 16 + " 🔍 SEARCH CONTACT " + "═" * 16)

        print("\n" + "─" * 38)
        search_record = input("🔎 Enter the name or number to search:\n")
        print("─" * 38)

        found = False

        if (search_record.isdigit()):
            for key, value in self.contacts.items():
                if (search_record == value):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {key}")
                    print(f"📞 Number : {value}")
                    print("=" * 22 + "\n")
                    self.battery_manager.consume_battery(2)
                    return

            for call in self.call_list:
                if (search_record == call["number"]):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {call['name']}")
                    print(f"📞 Number : {call['number']}")
                    print("=" * 22 + "\n")
                    self.battery_manager.consume_battery(2)
                    return

        else:
            for key, value in self.contacts.items():
                if (search_record == key):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {search_record}")
                    print(f"📞 Number : {self.contacts[search_record]}")
                    print("=" * 22 + "\n")
                    self.battery_manager.consume_battery(2)
                    return

            for call in self.call_list:
                if (search_record == call["name"]):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {call['name']}")
                    print(f"📞 Number : {call['number']}")
                    print("=" * 22 + "\n")
                    self.battery_manager.consume_battery(2)
                    return

        if not found:
            print("\n❌ Contact not found.\n")

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
                    self.battery_manager.consume_battery(2)
                    return
                elif (sure_thing == "n"):
                    return
                else:
                    print("Enter a valid choice")                         

    def contact_manager(self):
        if not self.battery_manager.check_battery():
            return
        self.see_contact_menu()

        while True :
            choice=input("\n➡️  Enter your choice : ")
            print()

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
                    self.see_contact_menu()
                elif choice == 7 :
                    return
                else:
                    print("Enter a valid choice")
            else:
                print("Error : Choice should be a digit")        
