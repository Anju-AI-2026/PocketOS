class BatteryManager:

    def __init__(self):
        self.battery = 100

    def see_battery_menu(self):
        print("="*35)
        print("            BATTERY MENU")
        print("="*35)
        print("1.Charge battery")
        print("2.Show battery")    
        print("3.Back")

    def show_battery(self):
        print("Current Battery :",self.battery)

    # Method to recharge the battery
    def charge_battery(self):
        if (self.battery == 100):
            print("Battery is already full !!")
            return
        if (self.battery < 100):
            charge = int(input("Enter the battery parcentage to charge below 100 :"))
            if (charge > 100):
                print("Please enter battery below 100")    
            else:
                print("Current battery :",self.battery)
                print("Charge amount :", charge)
                self.battery = self.battery+charge   
                if (self.battery > 100):
                    self.battery = 100 
                print("\nBattery charged successfully.")
                print("Current battery :", self.battery)   

    # Method to protect the battery 
    def protect_battery(self):
        if self.battery < 0 :
            self.battery = 0
            return      

    def consume_battery(self, amount):
        self.battery -= amount
        self.protect_battery()     

    def check_battery(self):
        if self.battery == 0:
            print("Phone is switched off.")
            print("Please charge the battery.")
            return False

        if self.battery <= 20:
            print("Battery is getting low! Please charge your phone.")

        return True 
