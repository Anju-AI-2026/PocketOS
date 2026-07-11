from phone_class import Phone

# Password authentication before accessing the phone
real_p=12345   
password=int(input("Enter the password : "))
if(real_p==password):
    print("The password is correct")
else:
    print("The password is incorrect")   
    exit() 

# Taking phone details from the user
name=input("Enter the phone company name : ")
brand=input("Enter the mobile phone brand name : ")
colour=input("Enter the mobile phone colour : ")
memory=input("Enter the memory of the mobile phone : ")

# Creating a Phone object
phone1=Phone(name,brand,colour,memory)

# Displaying menu repeatedly until the user exits the program
print("========Menu========")
print("1.Show the details of the Mobile phone")
print("2.Make a call")
print("3.Send a message")
print("4.Play a music")
print("5.Show call history")
print("6.Show phone battery")
print("7.Charge battery")
print("8.See menu")
print("9.Add Contact")
print("10.View saved contact")
print("11.Delete contact")
print("12.Search contact") 
print("13.View message history") 
print("14.Delete message")
print("15.Calculator")
print("16.Games")
print("17.Exit") 

# Processing user's menu choice
while True:

    choice=int(input("Enter a choice number from the menu : "))

    if phone1.battery > 20:
        if choice==1:
            phone1.showdetails()
        elif choice==2:
            phone1.call()
        elif choice==3:
            phone1.message()
        elif choice==4:
            phone1.playmusic()
        elif choice==5:
            print(phone1.view_call_history()) 
        elif choice==6:
            print(phone1.battery)
        elif choice==7:
            phone1.charge_phone()
        elif choice == 8:
            phone1.see_menu()  
        elif choice == 9:
            phone1.add_contact() 
        elif choice == 10:
            phone1.view_contact()  
        elif choice == 11:
            phone1.delete_contact() 
        elif choice == 12:
            phone1.search_contact() 
        elif choice == 13:
            phone1.view_message_history()  
        elif choice == 14:
            phone1.delete_message() 
        elif choice == 15:
            phone1.calculator()
        elif choice == 16:
            phone1.games()
        elif choice == 17:
            exit()    
        else:
            print("Please enter a valid number!!!")                    
    else:
        print("Battery running slow please charge it.\n current battery :  ",phone1.battery)
        exit()

if __name__ == "__main__":
    main()
