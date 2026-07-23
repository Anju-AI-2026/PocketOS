from phone_class import Phone

# Interface of the main page of the phone
print("="*70)
print("\n                        📱 PHONE MANAGEMENT SYSTEM\n")
print("="*70)

print()
print("                  ----------------------------")
print("                 |                            |")
print("                 |🔐  PASSWORD ATHENTICATION  |")
print("                 |                            |")
print("                  ----------------------------")

# Password authentication before accessing the phone
real_p=12345   

while True:
    
    password=input("\nEnter the password 🗝️  : ")

    if (password.isdigit()):
        password = int(password)
        if(real_p==password):
            print("\n✅ Access Granted!")
            break
        else:
            print("\n❌Incorrect password")
    else:
        print("\nThe password should contain digits only")

input("\nPress Enter to Continue...")

# Creating a Phone object
phone1=Phone(name,brand,colour,memory)

# Displaying menu repeatedly until the user exits the program
phone1.see_menu()
print()
print("-"*35)
print()
print("📱 Which application would you like to open?\n")
# Processing user's menu choice
while True:
    
    choice=int(input("➡️  Enter a choice : "))
    print()

    if not phone1.battery_manager.check_battery():
        continue
    if choice==1:
        phone1.showdetails()
    elif choice==2:
        phone1.contact_manager()
    elif choice==3:
        phone1.call_manager()
    elif choice==4:
        phone1.message_manager()
    elif choice==5:
        phone1.music_manager() 
    elif choice==6:
        phone1.calculator_manager()
    elif choice==7:
        phone1.game_manager()
    elif choice == 8:
        phone1.battery_manager.show_battery()
    elif choice == 9:
        phone1.battery_manager.battery_manager()
    elif choice == 11:
        exit()
    else:
        print("Please enter a valid number!!!")                    

if __name__ == "__main__":
    main()
