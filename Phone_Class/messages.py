# Message manager class to handle messaging features

class MessageManager:

    # Constructor to initialize message storage and battery manager
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager
        self.message_list=[]

    # Method to see the message menu
    def see_message_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                  ✉️ MESSAGE MANAGER                   ║")
        print("╠" + "═"*54 + "╣") 
        print("║  1. ✉️  Send a Message                                ║")
        print("║  2. 📥 Inbox                                         ║")
        print("║  3. 🗑️  Delete Message                                ║")
        print("║  4. 🧹 Clear Messages                                ║")
        print("║  5. 📋 Show Menu                                     ║")
        print("║  6. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")

    # Method to send messages and store message history
    def message(self):
        print("\n" + "═"*16 + " ✉️ SEND A MESSAGE " + "═"*16 + "\n")

        while True:
            print("─"*50)
            user_choice = (input("📞 Enter the contact name or phone number:\n"))
            print("─"*50)

            # Validate user input
            if (user_choice.isdigit()):
                if (len(user_choice)==10):
                    for key,value in self.contacts.items():
                        if (value == user_choice):
                            print("\n" + "═"*35)
                            msg = input(f"💬 Enter the message for {key}:\n")
                            print("═"*35 + "\n")

                            # Save the operation in history
                            message_chat = {
                                "name" : key,
                                "number" : value,
                                "message" : msg,
                                "type" : "Sent"
                            }

                            print("─"*35)
                            print("✅ Message sent successfully!\n")
                            print(f"👤 Contact : \n{user_choice}\n")
                            print(f"💬 Message :\n{msg}")
                            print("─"*35)

                            self.message_list.append(message_chat)
                            self.battery_manager.consume_battery(5)
                            return

                    while True:
                        save_choice = input("💾 Save this number to contacts? (y/n): ").lower()

                        if (save_choice.isalpha()):
                            if save_choice == "y":

                                while True:
                                    name = input("👤 Enter contact name:\n")

                                    # Validate user input
                                    if (name.replace(" ","").isalnum()):
                                        if(name.isdigit()):
                                            print("\n❌ Invalid Input")
                                            print("Contact name cannot contain only numbers.\n")
                                        else:
                                            msg = input("💬 Enter your message:\n")

                                            # Save the operation in history
                                            message_chat = {
                                                "name" : name,
                                                "number" : user_choice,
                                                "message" : msg,
                                                "type" : "Sent"
                                            }

                                            print("─"*35)
                                            print("✅ Message sent successfully!\n")
                                            print(f"👤 Contact : \n{name}\n")
                                            print(f"💬 Message :\n{msg}")
                                            print("─"*35)

                                            self.message_list.append(message_chat)
                                            self.contacts[name] = user_choice
                                            self.battery_manager.consume_battery(5)
                                            return
                                    else:
                                        print("\n❌ Invalid Input")
                                        print("Name should contain only letters or alphanumeric characters.\n")

                            elif (save_choice == "n"):
                                msg = input("💬 Enter the message for the unknown number:\n")

                                # Save the operation in history
                                message_chat = {
                                    "name" : "Unknown",
                                    "number" : user_choice,
                                    "message" : msg,
                                    "type" : "Sent"
                                }

                                print("─"*35)
                                print("✅ Message sent successfully!\n")
                                print("👤 Contact : \nUnknown Number\n")
                                print(f"💬 Message :\n{msg}")
                                print("─"*35)

                                self.message_list.append(message_chat)
                                self.battery_manager.consume_battery(5)
                                return

                            else:
                                print("\n❌ Invalid Input")
                                print("Please enter a valid choice.\n")

                        else:
                            print("\n❌ Invalid Input")
                            print("Please enter a valid choice.\n")

                else:
                    print("\n❌ Invalid Input")
                    print("Phone number must contain exactly 10 digits.\n")

            else:
                if(user_choice in self.contacts):
                    msg = input(f"💬 Enter the message for {user_choice}: ")

                    # Save the operation in history
                    message_chat = {
                        "name" : user_choice,
                        "number" : self.contacts[user_choice],
                        "message" : msg,
                        "type" : "Sent"
                    }

                    print("─"*35)
                    print("✅ Message sent successfully!\n")
                    print(f"👤 Contact :\n {user_choice}\n")
                    print(f"💬 Message :\n{msg}")
                    print("─"*35)

                    self.message_list.append(message_chat)
                    self.battery_manager.consume_battery(5)
                    return

                else:
                    print("\n" + "="*22)
                    print("❌ Contact not found.")
                    print("="*22 + "\n")

    # Method to display message history
    def view_message_history(self):
        print("\n" + "═"*17 + " 📥 MESSAGE INBOX " + "═"*17 + "\n")
        self.battery_manager.consume_battery(2)

        if not self.message_list:
            print("╔══════════════════════════════╗")
            print("║    📭 No Messages Found      ║")
            print("╚══════════════════════════════╝\n")
            return

        print("╔════════════════════════════════════╗")
        print("║          📨 MESSAGE INBOX          ║")
        print("╚════════════════════════════════════╝\n")

        # Display stored records
        for index, message in enumerate(self.message_list, start=1):
            print(f"📩 Message #{index}")
            print(f"👤 Name    : {message['name']}")
            print(f"📞 Number  : {message['number']}")
            print(f"💬 Message : {message['message']}")
            print(f"📤 Type    : {message['type']}")
            print("─" * 35)

    # Method to delete a individual message from history
    def delete_message(self):
        print("\n" + "═"*15 + " 🗑️ DELETE MESSAGE " + "═"*15 + "\n")

        if (not self.message_list):
            print("╔══════════════════════════════╗")
            print("║   📭 Message History Empty   ║")
            print("╚══════════════════════════════╝\n")
        else:
            while True:
                contact_name = input("👤 Enter the contact name to delete:\n")

                # Validate user input
                if (contact_name.isalnum()):
                    for i, message in enumerate(self.message_list):
                        if contact_name == message["name"]:
                            del self.message_list[i]
                            print("\n✅ Message deleted successfully!\n")
                            self.battery_manager.consume_battery(2)
                            return

                    print("\n❌ Contact not found.\n")

                else:
                    print("\n❌ Invalid Input")
                    print("Name should contain only alphanumeric characters.\n")

    # Method to clear the message history
    def clear_message_history(self):
        print("\n" + "═"*14 + " 🧹 CLEAR MESSAGES " + "═"*14 + "\n")

        if (not self.message_list):
            print("╔════════════════════════════════════╗")
            print("║   📭 No Messages To Clear          ║")
            print("╚════════════════════════════════════╝\n")
            return

        else:
            while True:

                # Confirm before deleting all records
                sure_thing = input("⚠️  Are you sure? (y/n): ").lower()

                if (sure_thing == "y"):
                    self.message_list.clear()
                    print("\n✅ Message history cleared successfully.\n")
                    self.battery_manager.consume_battery(2)
                    return

                elif (sure_thing == "n"):
                    return

                else:
                    print("\n❌ Please enter a valid choice.\n")

    # Method to create the message controller
    def message_manager(self):
        if not self.battery_manager.check_battery():
            return

        self.see_message_menu()

        while True:
            print("\n" + "─"*42)
            print("📱 What would you like to do?")
            print("─"*42)

            choice = input("\n➡️  Enter your choice: ")

            if choice.isdigit():
                choice = int(choice)

                if choice == 1:
                    self.message()
                elif choice == 2:
                    self.view_message_history()
                elif choice == 3:
                    self.delete_message()
                elif choice == 4:
                    self.clear_message_history()
                elif choice == 5:
                    self.see_message_menu()
                elif choice == 6:
                    return
                else:
                    print("\n❌ Please enter a valid menu choice.\n")
            else:
                print("\n❌ Error: Choice must be a digit.\n")
