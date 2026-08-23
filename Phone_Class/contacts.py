# Contact manager class to store and manage contacts

from storage import save_contacts, load_contacts

class ContactManager:

    # Constructor to initialize contact storage and battery manager

    def __init__(self, battery_manager):
        self.contacts = load_contacts()
        self.battery_manager = battery_manager

    # Healper method for name lower case and upper case problem solving
    def find_contact(self, name):

        for stored_name in self.contacts:

            if stored_name.lower() == name.lower():
                return stored_name

        return None    

    # Method to display the contact menu
    def see_contact_menu(self):
        print(f"\n🔋 Battery: {self.battery_manager.battery}%\n")
        print("╔" + "═"*54 + "╗")
        print("║                  📇 CONTACT MANAGER                  ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. ➕ Add Contact                                   ║")
        print("║  2. 👀 View Contacts                                 ║")
        print("║  3. 🗑️  Delete Contact                                ║")
        print("║  4. 🔍 Search Contact                                ║")
        print("║  5. 🧹 Clear Contacts                                ║")
        print("║  6. ✏️  Edit Contacts                                 ║")
        print("║  7. 📋 Show Menu                                     ║")
        print("║  8. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")

    # Adds a contact after validating the name and phone number
    def add_contact(self):
        print("\n" + "═" * 18 + " ➕ ADD CONTACT " + "═" * 18)
        if not self.battery_manager.consume_battery(2):
            return

        while True:
            print()
            name = input("👤 Enter contact name:\n")

            if self.find_contact(name) is not None:
                print("\n❌ Contact already exists.\n")
                return
            else:
                # Validate user input
                if (name.replace(" ", "").isalnum()):
                    if (name.isdigit()):
                        print("\n❌ Invalid input.")
                        print("Name cannot contain only numbers.\n")
                    else:
                        break
                else:
                    print("\n❌ Invalid input.")
                    print("Name can contain only letters or alphanumeric characters.\n")

        while True:
            phone_number = input("\n📞 Enter phone number:\n")

            # Validate user input
            if phone_number.isdigit():
                if (len(phone_number) == 10):
                    if phone_number in self.contacts.values():
                        print("\n❌ This phone number already exists.")
                    else:
                        # Save the operation in history
                        self.contacts[name] = phone_number
                        save_contacts(self.contacts) 
                        print("\n✅ Contact added successfully!\n")
                        if not self.battery_manager.consume_battery(2):
                            return
                        break
                else:
                    print("❌ Phone number must contain exactly 10 digits.")
            else:
                print("❌ Phone number should contain numbers only.")

    # Displays all contacts stored in the contact book
    def view_contact(self):
        print("\n" + "═" * 17 + " 👀 VIEW CONTACTS " + "═" * 17)

        if not self.battery_manager.consume_battery(2):
            return

        if (not self.contacts):
            print("\n📭 Contact book is empty.\n")
        else:
            print("\n" + "─" * 22)
            print("📖 CONTACT BOOK")
            print("─" * 22)

            # Display stored records
            count = 1
            for key, value in self.contacts.items():
                print(f"\n📌 Contact {count}")
                print(f"👤 Name   : {key}")
                print(f"📞 Number : {value}")
                print("─" * 24)
                count = count + 1

    # Method to delete the contact from the contact
    def delete_contact(self):
        print("\n" + "═" * 16 + " 🗑️  DELETE CONTACT " + "═" * 16)

        if not self.battery_manager.consume_battery(2):
            return

        if (not self.contacts):
            print("\n📭 Contact book is empty.\n")
        else:
            while True:
                print("\n" + "─" * 45)
                contact_name = input("👤 Enter the contact name to delete:\n")
                contact_key = self.find_contact(contact_name)
                print("─" * 45)

                # Validate user input
                if contact_name.replace(" ", "").isalnum():
                    if contact_key is not None:
                        del self.contacts[contact_key]
                        save_contacts(self.contacts)
                        print("\n✅ Contact deleted successfully!\n")
                        if not self.battery_manager.consume_battery(2):
                            return
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
        contact_key = self.find_contact(search_record)
        print("─" * 38)

        if (not self.contacts):
            print("\n📭 Contact book is empty.\n")
            return

        found = False

        if (search_record.isdigit()):
            for key, value in self.contacts.items():
                if (search_record == value):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {key}")
                    print(f"📞 Number : {value}")
                    print("=" * 22 + "\n")
                    found = True
                    if not self.battery_manager.consume_battery(2):
                        return

            for call in self.call_list:
                if (search_record == call["number"]):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {call['name']}")
                    print(f"📞 Number : {call['number']}")
                    print("=" * 22 + "\n")
                    found = True
                    if not self.battery_manager.consume_battery(2):
                        return

        else:
            if contact_key is not None:
                print("\n" + "=" * 22)
                print("✅ Search successful!\n")
                print(f"👤 Name   : {contact_key}")
                print(f"📞 Number : {self.contacts[contact_key]}")
                print("=" * 22 + "\n")
                found = True
                if not self.battery_manager.consume_battery(2):
                    return

            for call in self.call_list:
                if (search_record.lower() == call["name"].lower()):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {call['name']}")
                    print(f"📞 Number : {call['number']}")
                    print("=" * 22 + "\n")
                    found = True
                    if not self.battery_manager.consume_battery(2):
                        return

        if not found:
            print("\n❌ Contact not found.\n")

    # Method to create the clear the contact
    def clear_contact(self):
        print("\n" + "═" * 17 + " 🧹 CLEAR CONTACTS " + "═" * 17)

        if (not self.contacts):
            print("\n📭 Contact book is empty. Nothing to clear.\n")
            return
        else:
            while True:

                # Confirm before deleting all records
                print("\n" + "─" * 28)
                sure_thing = input("⚠️  Are you sure? (y/n): ").lower()
                print("─" * 28)

                if (sure_thing == "y"):
                    self.contacts.clear()
                    save_contacts(self.contacts)
                    print("\n✅ All contacts deleted successfully!\n")
                    if not self.battery_manager.consume_battery(2):
                        return

                elif (sure_thing == "n"):
                    return

                else:
                    print("\n❌ Please enter a valid choice.\n")

    # Method to edit an existing contact
    def edit_contact(self):
        if not self.contacts:
            print("\n📭 Contact list is empty.\n")
            return

        print("\n" + "═" * 16 + " 📇 CONTACTS " + "═" * 16 + "\n")

        for name, number in self.contacts.items():
            print(f"👤 {name} - {number}")

        contact_name = input("\n✏️ Enter the contact name to edit: ").strip()

        contact_key = self.find_contact(contact_name)

        if contact_key is None:
            print("\n❌ Contact not found.\n")
            return

        old_number = self.contacts[contact_key]

        # Get new name
        while True:
            new_name = input("New name (leave empty to keep same): ").strip()

            if new_name == "":
                new_name = contact_key
                break

            elif self.find_contact(new_name) is not None and self.find_contact(new_name) != contact_key:
                print("\n❌ Contact already exists.\n")

            elif new_name.replace(" ", "").isalnum():
                if new_name.isdigit():
                    print("\n❌ Invalid input.")
                    print("Name cannot contain only numbers.\n")
                else:
                    break

            else:
                print("\n❌ Invalid input.")
                print("Name can contain only letters or alphanumeric characters.\n")

        # Get new number
        while True:
            new_number = input("New number (leave empty to keep same): ").strip()

            if new_number == "":
                new_number = old_number
                break

            elif new_number.isdigit():
                if len(new_number) == 10:
                    if new_number in self.contacts.values() and new_number != old_number:
                        print("\n❌ This phone number already exists.")
                    else:
                        break
                else:
                    print("\n❌ Phone number must contain exactly 10 digits.")

            else:
                print("\n❌ Phone number should contain numbers only.")

        # Update contact
        del self.contacts[contact_key]
        self.contacts[new_name] = new_number

        save_contacts(self.contacts)

        print("\n✅ Contact updated successfully!\n")

        if not self.battery_manager.consume_battery(2):
            return            

    # Method to control all contact operations
    def contact_manager(self):

        self.see_contact_menu()

        while True:
            if not self.battery_manager.check_battery():
                return
            print("\n" + "─" * 35)
            print("📱 What would you like to do?")
            print("─" * 35)

            choice = input("\n➡️  Enter your choice: ")
            print()

            if (choice.isdigit()):
                choice = int(choice)

                if choice == 1:
                    self.add_contact()
                elif choice == 2:
                    self.view_contact()
                elif choice == 3:
                    self.delete_contact()
                elif choice == 4:
                    self.search_contact()
                elif choice == 5:
                    self.clear_contact()
                elif choice == 6:
                    self.edit_contact()    
                elif choice == 7:
                    self.see_contact_menu()
                elif choice == 8:
                    return
                else:
                    print("❌ Enter a valid choice.")
            else:
                print("❌ Error: Choice should be a digit.")
