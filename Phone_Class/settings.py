# Settings manager class

from storage import save_password, load_password

class SettingsManager:

    # Constructor to initialize battery manager
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager

        self.real_password = storage.load_password()

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
    # Method to show the settings menu 
    def settings_menu(self):
        print("\n" + "═" * 14 + " ⚙️ SETTINGS " + "═" * 14 + "\n")
        
        print("1. 🔐 Change Password")
        print("2. 📦 Reset All Data")
        print("3. 📱 Show System Status")
        print("4. ℹ️ About PocketOS")
        print("5. 🔙 Back")

    # Method to display settings menu
    def settings_manager(self):

        self.settings_menu()
        print(f"\n🔋 Battery: {self.battery_manager.battery}%\n")
        while True:

            choice = input("\n👉 Enter your choice: ")

            if choice == "1":
                self.change_password()   

            elif choice == "5":
                break

            else:
                print("\n🚧 Feature coming soon...\n")     

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
                                        save_password(new_password)
                                        self.real_password = new_password
                                        print("Password changed sucessefully !")
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
        pass
