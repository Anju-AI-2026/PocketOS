class CallManager:

    def __init__(self, battery_manager):
        self.battery_manager = battery_manager
        self.call_list=[]

    # Method to create the call menu
    def see_call_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                    📞 CALL MANAGER                  ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. 📲 Make a Call                                  ║")
        print("║  2. 👀 View Call History                            ║")
        print("║  3. 🗑️ Delete Call History                          ║")
        print("║  4. 🧹 Clear Call History                           ║")
        print("║  5. 📋 Show Menu                                    ║")
        print("║  6. 🔙 Back                                         ║")
        print("╚" + "═"*54 + "╝\n")

    # Method to make a phone call and store call history
    def call(self):
        while True:
            print("\n" + "═"*18 + " 📲 MAKE A CALL " + "═"*18 + "\n")

            user_choice=(input("📞 Enter the contact name or phone number:\n"))
            if (user_choice.isdigit()):
                if (len(user_choice)==10):
                        for key,value in self.contacts.items():
                            if (value == user_choice):
                                print(f"\n📞 Calling {key}...")
                                print("☎️  Dialing...\n")
                                print("✅ Call ended successfully.\n")

                                call_record = {
                                    "name" : key ,
                                    "number" : value,
                                    "type" : "Outgoing"
                                }
                                self.call_list.append(call_record)
                                self.battery_manager.consume_battery(5)
                                return
                        while True:
                            print("\n" + "─"*50)
                            save_choice = input("💾 Save this number to contacts? (y/n): ").lower()
                            print("─"*50)
                            if (save_choice.isalpha()):
                                if save_choice == "y":
                                    while True:
                                        print("\n" + "═"*27)
                                        name=input("👤 Enter contact name:\n")
                                        print("═"*27 + "\n")
                                        if (name.replace(" ","").isalnum()):
                                            if (name.isdigit()):
                                                print("\n❌ Invalid Input")
                                                print("Contact name cannot contain only numbers.\n")
                                            else:
                                                call_record = {
                                                    "name" : name,
                                                    "number" : user_choice,
                                                    "type" : "Outgoing"
                                                }
                                                self.call_list.append(call_record)
                                                self.contacts[name] = user_choice
                                                self.battery_manager.consume_battery(5)
                                                print("\n✅ Contact saved successfully!")
                                                print(f"\n📞 Calling {name}...")
                                                print("☎️  Dialing...\n")
                                                print("✅ Call ended successfully.\n")
                                                self.battery_manager.consume_battery(5)
                                                return
                                        else:
                                            print("\n❌ Invalid Input")
                                            print("Name should contain only letters or alphanumeric characters.\n")
                                elif (save_choice == "n"):
                                    print("\n📞 Calling Unknown Number...")
                                    print("☎️  Dialing...\n")
                                    print("✅ Call ended successfully.\n")
                                    call_record = {
                                        "name" : "Unknown",
                                        "number" : user_choice,
                                        "type" : "Outgoing"
                                    }
                                    self.call_list.append(call_record)
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
                if (user_choice in self.contacts):
                    print(f"\n📞 Calling {user_choice}...")
                    print("☎️  Dialing...\n")
                    print("✅ Call ended successfully.\n")
                    call_record={
                        "name" : user_choice,
                        "number" : self.contacts[user_choice],
                        "type" : "Outgoing"
                    }
                    self.call_list.append(call_record)
                    self.battery_manager.consume_battery(5)
                    return
                else:
                    print("\n" + "="*22)
                    print("❌ Contact not found.")
                    print("="*22 + "\n")

    # Method to display call history
    def view_call_history(self):
        print("\n" + "═"*15 + " 👀 CALL HISTORY " + "═"*15 + "\n")
        self.battery_manager.consume_battery(2)

        if not self.call_list:
            print("╔══════════════════════════════╗")
            print("║   📭 No Call History Found   ║")
            print("╚══════════════════════════════╝")
            return

        print("╔════════════════════════════════════╗")
        print("║          📜 CALL HISTORY           ║")
        print("╚════════════════════════════════════╝\n")

        for index, call in enumerate(self.call_list, start=1):
            print(f"📌 Call #{index}")
            print(f"👤 Name   : {call['name']}")
            print(f"📞 Number : {call['number']}")
            print(f"📤 Type   : {call['type']}")
            print("─" * 35)

    # Method to delete a call history
    def delete_call_history(self):
        print("\n" + "═"*14 + " 🗑️ DELETE CALL HISTORY " + "═"*14 + "\n")

        if (not self.call_list):
            print("╔══════════════════════════════╗")
            print("║   📭 No Call History Found   ║")
            print("╚══════════════════════════════╝\n")
            return

        else:
            print("╔════════════════════════════════════╗")
            print("║      📜 CALL HISTORY RECORDS       ║")
            print("╚════════════════════════════════════╝\n")

            for index, call in enumerate(self.call_list, start=1):
                print(f"📌 Call #{index}")
                print(f"👤 Name   : {call['name']}")
                print(f"📞 Number : {call['number']}")
                print(f"📤 Type   : {call['type']}")
                print("─" * 35)

            while True:
                choice = input("🗑️ Enter the call number to delete: ")

                if (choice.isdigit()):
                    choice = int(choice)
                    length = len(self.call_list)

                    if (choice >= 1 and choice <= length):
                        del self.call_list[choice-1]
                        print("\n✅ Call history deleted successfully.\n")
                        self.battery_manager.consume_battery(2)
                        return
                    else:
                        print("\n❌ Invalid Input")
                        print("Call number is out of range.\n")
                        
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
