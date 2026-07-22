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
