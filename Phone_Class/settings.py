# Settings manager class

class SettingsManager:

    # Constructor to initialize battery manager
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager

    # Method to show the settings menu 
    def settings_menu(self):
        print("\n" + "═" * 14 + " ⚙️ SETTINGS " + "═" * 14 + "\n")
        
        print("1. 🔐 Change Password")
        print("2. 📦 Reset All Data")
        print("3. 📱 Show System Status")
        print("4. ℹ️ About PocketOS")
        print("5. 🔙 Back")
