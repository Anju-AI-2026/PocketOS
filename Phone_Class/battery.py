# Battery manager class to simulate battery behavior

from storage import save_battery, load_battery

class BatteryManager:

    # Constructor to initialize battery percentage
    def __init__(self):
        self.battery = load_battery()

    # Method to see the battery menu
    def see_battery_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                 🔋 BATTERY MANAGER                   ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. ⚡ Charge Battery                                ║")
        print("║  2. 🔋 Show Battery Status                           ║")
        print("║  3. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")

    # Method to show current battery
    def show_battery(self):
        print("\n🔋 Current Battery :", self.battery, "%\n")

    # Method to recharge the battery
    def charge_battery(self):
        if (self.battery == 100):
            print("\n🔋 Battery is already fully charged.\n")
            return

        if (self.battery < 100):
            charge = int(input("⚡ Enter the battery percentage to charge (below 100): "))

            if (charge > 100):
                print("\n❌ Please enter a value below 100.\n")

            else:
                print(f"\n🔋 Current Battery : {self.battery}%")
                print(f"⚡ Charge Amount   : {charge}%")

                self.battery = self.battery + charge

                if (self.battery > 100):
                    self.battery = 100
                    save_battery(self.battery)

                print("\n✅ Battery charged successfully.")
                print(f"🔋 Current Battery : {self.battery}%\n")

    # Method to protect the battery
    def protect_battery(self):
        if self.battery < 0:
            self.battery = 0
            return

    # Method to reduce battery percentage
    def consume_battery(self, amount):

        self.battery -= amount

        if self.battery < 0:
            self.battery = 0

        save_battery(self.battery)

        # If battery became 0, stop the operation
        if self.battery == 0:
            print("\n📴 Phone is switched off.")
            print("⚡ Please charge the battery.\n")
            return False

        # Show low battery warning
        if self.battery <= 10:
            print(f"\n🔋 Battery Level: {self.battery}%")
            print("⚠️ Low battery! Please charge your phone.\n")

        return True

    # Method to check battery status
    def check_battery(self):
        if self.battery == 0:
            print("\n📴 Phone is switched off.")
            print("⚡ Please charge the battery.\n")
            return False

        if self.battery <= 10:
            print(f"\n🔋 Battery Level: {self.battery}%")
            print("⚠️ Low battery! Please charge your phone.\n")

        return True

    # Method to manage battery options
    def battery_manager(self):
        if not self.check_battery():
            return

        self.see_battery_menu()

        while True:
            print("\n" + "─"*42)
            print("🔋 What would you like to do?")
            print("─"*42)

            choice = input("\n➡️  Enter your choice: ")

            if choice.isdigit():
                choice = int(choice)

                if choice == 1:
                    self.charge_battery()

                elif choice == 2:
                    self.show_battery()

                elif choice == 3:
                    return

                else:
                    print("\n❌ Please enter a valid menu choice.\n")

            else:
                print("\n❌ Error: Choice must be a digit.\n")
