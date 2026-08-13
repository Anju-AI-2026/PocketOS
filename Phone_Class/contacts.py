# Contact manager class to store and manage contacts

from storage import save_contacts, load_contacts, save_battery

class ContactManager:

    # Constructor to initialize contact storage and battery manager

    def __init__(self, battery_manager):
        self.contacts = load_contacts()
        self.battery_manager = battery_manager

    # Method to display the contact menu
    def see_contact_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                  📇 CONTACT MANAGER                  ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. ➕ Add Contact                                   ║")
        print("║  2. 👀 View Contacts                                 ║")
        print("║  3. 🗑️  Delete Contact                                ║")
        print("║  4. 🔍 Search Contact                                ║")
        print("║  5. 🧹 Clear Contacts                                ║")
        print("║  6. 📋 Show Menu                                     ║")
        print("║  7. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")

    # Adds a contact after validating the name and phone number
    def add_contact(self):
        print("\n" + "═" * 18 + " ➕ ADD CONTACT " + "═" * 18)
        self.battery_manager.consume_battery(2)
        save_battery(self.battery_manager.battery)

        while True:
            print()
            name = input("👤 Enter contact name:\n")

            if (name in self.contacts):
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
                        self.battery_manager.consume_battery(2)
                        save_battery(self.battery_manager.battery)
                        break
                else:
                    print("❌ Phone number must contain exactly 10 digits.")
            else:
                print("❌ Phone number should contain numbers only.")

    # Displays all contacts stored in the contact book
    def view_contact(self):
        print("\n" + "═" * 17 + " 👀 VIEW CONTACTS " + "═" * 17)

        self.battery_manager.consume_battery(2)
        save_battery(self.battery_manager.battery)

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
        self.battery_manager.consume_battery(2)
        save_battery(self.battery_manager.battery)

        if (not self.contacts):
            print("\n📭 Contact book is empty.\n")
        else:
            while True:
                print("\n" + "─" * 45)
                contact_name = input("👤 Enter the contact name to delete:\n")
                print("─" * 45)

                # Validate user input
                if contact_name.replace(" ", "").isalnum():
                    if (contact_name in self.contacts):
                        del self.contacts[contact_name]
                        save_contacts(self.contacts)
                        print("\n✅ Contact deleted successfully!\n")
                        self.battery_manager.consume_battery(2)
                        save_battery(self.battery_manager.battery)
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
                    self.battery_manager.consume_battery(2)
                    save_battery(self.battery_manager.battery)
                    return

            for call in self.call_list:
                if (search_record == call["number"]):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {call['name']}")
                    print(f"📞 Number : {call['number']}")
                    print("=" * 22 + "\n")
                    self.battery_manager.consume_battery(2)
                    save_battery(self.battery_manager.battery)
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
                    save_battery(self.battery_manager.battery)
                    return

            for call in self.call_list:
                if (search_record == call["name"]):
                    print("\n" + "=" * 22)
                    print("✅ Search successful!\n")
                    print(f"👤 Name   : {call['name']}")
                    print(f"📞 Number : {call['number']}")
                    print("=" * 22 + "\n")
                    self.battery_manager.consume_battery(2)
                    save_battery(self.battery_manager.battery)
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
                    self.battery_manager.consume_battery(2)
                    save_battery(self.battery_manager.battery)
                    return

                elif (sure_thing == "n"):
                    return

                else:
                    print("\n❌ Please enter a valid choice.\n")

    # Method to edit an existing contact
    def edit_contact(self):
        if not self.contact_list:
            print("\n📭 Contact list is empty.\n")
            return

        print("\n" + "═" * 16 + " 📇 CONTACTS " + "═" * 16 + "\n")

        for name, number in self.contact_list.items():
            print(f"👤 {name} - {number}")

        contact_name = input("\n✏️ Enter the contact name to edit: ").strip()

        if contact_name not in self.contact_list:
            print("\n❌ Contact not found.\n")
            return

    # Method to control all contact operations
    def contact_manager(self):
        if not self.battery_manager.check_battery():
            return

        self.see_contact_menu()

        while True:
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
                    self.see_contact_menu()
                elif choice == 7:
                    return
                else:
                    print("❌ Enter a valid choice.")
            else:
                print("❌ Error: Choice should be a digit.")
