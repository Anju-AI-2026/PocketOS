# Settings manager class

import json
import storage

class SettingsManager:

    # Constructor to initialize battery manager
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager 

        self.real_password = storage.load_password()

        self.name = "Samsung"
        self.brand = "Galaxy S24"
        self.colour = "Black"
        self.memory = "256 GB"

     # Password authentication before accessing the phone
    def authenticate_password(self):

        while True:

            password = input("\n🗝️  Enter your password: ")

            if (password.isdigit()):
                password = int(password)

                if (self.real_password == password):
                    print("\n✅ Access Granted. Welcome!\n")
                    break
                else:
                    print("\n❌ Incorrect password. Please try again.")

            else:
                print("\n❌ Password should contain digits only.")

    # Method to display the settings menu
    def settings_menu(self):

        print(f"\n🔋 Battery: {self.battery_manager.battery}%\n")

        print("╔" + "═"*54 + "╗")
        print("║                    ⚙️ SETTINGS                        ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. 🔐 Change Password                               ║")
        print("║  2. 📦 Reset All Data                                ║")
        print("║  3. 📱 Show System Status                            ║")
        print("║  4. ℹ️  About PocketOS                                ║")
        print("║  5. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")  

    # Method to change the password
    def change_password(self):

        while True:

            password = input("\n🗝️  Enter the current password: ")

            if (password.isdigit()):
                password = int(password)

                if self.real_password == password:
                    print("\n✅ Password is correct !\n")

                    while True :
                            
                        new_password = input("\nEnter the new password :")

                        if (new_password.isdigit()):

                            new_password = int(new_password)

                            while True :
                                confirm_password = input("\nEnter the password again :")

                                if (confirm_password.isdigit()):

                                    confirm_password = int(confirm_password)

                                    if (confirm_password == new_password):
                                        storage.save_password(new_password)
                                        self.real_password = new_password
                                        print("Password changed sucessefully !")
                                        if not self.battery_manager.consume_battery(2):
                                            return
                                        return
                                    else:
                                        print("\n❌The password is not same. Please enter again!")
                                        break
                                else:
                                    print("\n❌ Password is incorrect. Only enter digit!")        
                        else:
                            print("\n❌ Password is incorrect. Only enter digit!")
                else:
                    print("\n❌ Password is incorrect.")
            else:
                print("\n❌ Password is incorrect. Only enter digit!")

    def reset_data(self):

        while True:

            # Load existing data before resetting
            contacts = storage.load_contacts()
            contact_count = len(contacts)

            calls = storage.load_calls()
            call_count = len(calls)

            messages = storage.load_messages()
            message_count = len(messages)

            calculations = storage.load_calculations()
            calculation_count = len(calculations)

            songs = storage.load_music()
            song_count = len(songs["playlist"])

            # Check whether there is any user data
            if (contact_count == 0 and
                call_count == 0 and
                message_count == 0 and
                calculation_count == 0 and
                song_count == 0):

                print("\nℹ️ There is no user data to reset.")
                return

            # Show existing data before confirmation
            print("\n" + "═" * 18 + " ⚠️ RESET DATA " + "═" * 18)
            print(f"\n📇 Contacts      : {contact_count}")
            print(f"📞 Calls         : {call_count}")
            print(f"💬 Messages      : {message_count}")
            print(f"🧮 Calculations  : {calculation_count}")
            print(f"🎵 Music Tracks  : {song_count}")

            print("\n⚠️ This will permanently clear all user data.")

            sure_thing = input("\nAre you sure? (y/n): ").lower()

            if sure_thing == "y":

                # Reset contacts
                with open(storage.CONTACTS_FILE, "w") as file:
                    json.dump({}, file, indent=4)

                # Reset calls
                with open(storage.CALLS_FILE, "w") as file:
                    json.dump([], file, indent=4)

                # Reset messages
                with open(storage.MESSAGES_FILE, "w") as file:
                    json.dump([], file, indent=4)

                # Reset calculations
                with open(storage.CALCULATOR_FILE, "w") as file:
                    json.dump([], file, indent=4)

                # Reset battery
                with open(storage.BATTERY_FILE, "w") as file:
                    json.dump({"level": 20}, file, indent=4)

                # Reset music
                with open(storage.MUSIC_FILE, "w") as file:
                    json.dump({
                        "playlist": {},
                        "current_song": None
                    }, file, indent=4)

                # Keep current password
                with open(storage.PASSWORD_FILE, "w") as file:
                    json.dump({
                        "password": self.real_password
                    }, file, indent=4)

                # Consume battery for the reset operation
                if not self.battery_manager.consume_battery(10):
                    return

                # Show reset result
                print("\n" + "═" * 18 + " ✅ DATA CLEARED " + "═" * 18)

                print(f"\n📇 Contacts Cleared      : {contact_count}")
                print(f"📞 Calls Cleared         : {call_count}")
                print(f"💬 Messages Cleared     : {message_count}")
                print(f"🧮 Calculations Cleared : {calculation_count}")
                print(f"🎵 Music Tracks Cleared : {song_count}")

                print("\n🔋 Battery reset to 20%")
                print("🔐 Password preserved 🔒")

                print("\n✅ All selected data has been reset successfully!")

                return

            elif sure_thing == "n":

                print("\n↩️ Reset cancelled. No data was changed.")
                return

            else:

                print("\n❌ Invalid choice! Please enter y or n.")

    def show_system_status(self):
        print("\n" + "─" * 20 + " System Status " + "─" * 20)
        print(f"🔋 Battery: {self.battery_manager.battery}%")
        print(f"🔐 Password set: {'Yes Protected ✅' if self.real_password is not None else 'No'}")

        contacts = storage.load_contacts()
        count = len(contacts)
        print("💾 Contacts Stored :",count)

        calls = storage.load_calls()
        count = len(calls)
        print("📞 Calls Stored :",count)

        messages = storage.load_messages()
        count = len(messages)
        print("💬 Messages Stored :",count)

        calculations = storage.load_calculations()
        count = len(calculations)
        print("🧮 Calculations Stored :",count)

        songs = storage.load_music()
        count = len(songs["playlist"])
        current_song = songs["current_song"]

        print("🎵 Music Tracks :",count)
        print("🎵 Current Music :",current_song)

        print("📱 PocketOS Version   : v2.0 ")

        print("⚙️ System State       : Active ✅")

        print("─" * 50)

    # Method to display phone information
    def showdetails(self):
        if not self.battery_manager.consume_battery(5):
            return

        print("╔" + "═"*54 + "╗")
        print("║                📱 PHONE INFORMATION                  ║")
        print("╠" + "═"*54 + "╣")
        print(f"║  🏢 Company : {self.name:<37}  ║")
        print(f"║  📱 Model   : {self.brand:<37}  ║")
        print(f"║  🎨 Colour  : {self.colour:<37}  ║")
        print(f"║  💾 Storage : {self.memory:<37}  ║")
        print("╚" + "═"*54 + "╝")    

    # Method to display settings menu
    def settings_manager(self):

        self.settings_menu()

        while True:
            if not self.battery_manager.check_battery():
                return

            print("\n" + "─"*42)
            print("📱 What would you like to do?")
            print("─"*42)
        
            choice = input("\n➡️  Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)

                if choice == 1 :
                    self.change_password()

                elif choice == 2 :
                    self.reset_data()  

                elif choice == 3 :
                    self.show_system_status()     

                elif choice == 4 :
                    self.showdetails()     

                elif choice == 5 :
                    break

                else:
                    print("\n❌ Please enter a valid menu choice.\n")
            else:
                print("\n❌ Error: Choice must be a digit.\n")   
