from phone_class import Phone

# Main interface of the Phone Management System
print("╔" + "═"*68 + "╗")
print("║               📱 PHONE MANAGEMENT SYSTEM                ║")
print("╚" + "═"*68 + "╝")

print()
print("             ╔══════════════════════════════════════╗")
print("             ║        🔐 PASSWORD AUTHENTICATION    ║")
print("             ╚══════════════════════════════════════╝")

# Password authentication before accessing the phone
real_p = 12345

while True:

    password = input("\n🗝️  Enter your password: ")

    if (password.isdigit()):
        password = int(password)

        if (real_p == password):
            print("\n✅ Access Granted. Welcome!\n")
            break
        else:
            print("\n❌ Incorrect password. Please try again.")

    else:
        print("\n❌ Password should contain digits only.")

input("⏩ Press Enter to continue...")

# Creating a Phone object
phone1 = Phone()

# Displaying the menu until the user exits the program
phone1.see_menu()

print("\n" + "─"*45)
print("📱 Which application would you like to open?")
print("─"*45)

# Processing user's menu choice
while True:

    if not phone1.battery_manager.check_battery():
        break

    choice = input("\n➡️  Enter your choice: ")
    print()

    if (choice.isdigit()):

        choice = int(choice)

        if choice == 1:
            phone1.clear_screen()
            phone1.see_menu()
            phone1.showdetails()

        elif choice == 2:
            phone1.clear_screen()
            phone1.contact_manager()
            phone1.see_menu()

        elif choice == 3:
            phone1.clear_screen()
            phone1.call_manager()
            phone1.see_menu()

        elif choice == 4:
            phone1.clear_screen()
            phone1.message_manager()
            phone1.see_menu()

        elif choice == 5:
            phone1.clear_screen()
            phone1.music_manager()
            phone1.see_menu()

        elif choice == 6:
            phone1.clear_screen()
            phone1.calculator_manager()
            phone1.see_menu()

        elif choice == 7:
            phone1.clear_screen()
            phone1.game_manager()
            phone1.see_menu()

        elif choice == 8:
            phone1.clear_screen()
            phone1.battery_manager.show_battery()

        elif choice == 9:
            phone1.clear_screen()
            phone1.battery_manager.battery_manager()
            phone1.see_menu()
            
        elif choice == 10:
            exit()

        else:
            print("\n❌ Invalid choice!")
            print("Please enter a number between 1 and 10.\n")

    else:
        print("\n❌ Error: Choice must be a digit.\n")

if __name__ == "__main__":
    main()
