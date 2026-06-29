# Program to demonstrate a phone class 

class Phone:

     # Constructor to initialize phone details and default values
    def __init__(self,name,brand,colour,memory):
        self.name=name
        self.brand=brand
        self.colour=colour
        self.memory=memory
        self.call_list=[]
        self.message_list=[]
        self.contact={}
        self.battery=100

    # Method to display phone details
    def showdetails(self):
        print("Mobile Phone company name :",self.name)
        print("The mobile phone brand i : ",self.brand)
        print("The colour of the mobile phone",self.colour)
        print("The memory of the mobile phone is : ",self.memory)

    # Method to make a phone call and store call history
    def call(self):
        if self.battery>20:
            num=(input("Enter the phone number : +19"))    
            if (len(num)==10):
                print("Dailing!!!!!")
                self.call_list.append(num)
                self.battery=self.battery-10
            else:
                print("Enter the correct phone number")  
                return  
        else:
            print("Battery is running low. Please charge it")

    # Method to send messages and store message history
    def message(self):
        if self.battery>20:
            num=(input("Enter the phone number to send message : "))
            lenght=len(num)
            if (lenght==10):
                msg=input("Enter the message to send : ")    
                print("Message sent!!!")
                self.message_list.append((num,msg))
                if self.battery>0:
                    self.battery=self.battery-5
            else:
                print("Please enter the correct contact number")
                return
        else:
            print("Battery is running low. Please charge it")    

    # Method to play music and reduce battery percentage
    def playmusic(self):
        if self.battery>20:
            music=input("Enter the song name : ")
            print("Plyaing",music,"music") 
            if self.battery>0:
                self.battery=self.battery-15
        else:
            print("Battery is running low. Please charge it")

    # Method to recharge the battery
    def charge_phone(self):
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

    # Method to see the menu
    def see_menu(self):
        if (self.battery > 20):
            print("========Menu========")
            print("1.Show the details of the Mobile phone")
            print("2.Make a call")
            print("3.Send a message")
            print("4.Play a music")
            print("5.Show call history")
            print("6.Show message history")
            print("7.Show phone battery")
            print("8.Charge battery")
            print("9.See menu")
            print("10.Add Contact")
            print("11.View saved contact")
            print("12.Delete contact")
            print("13.Exit")
        else:
            print("Battery is running low. Please charge it")


    # Adds a contact after validating the name and phone number
    def add_contact(self):
        if (self.battery > 20):
            while True:
                name=input("Enter the contact name :")
                if (name.replace(" ","").isalnum()):
                    if (name.isdigit()):
                        print("Contact name should not be only made up of numbers!")
                    else:
                        break
                else:
                    print("Name only contain alpha+numeric name")

            while True:
                phone_number=input("Enter phone number :")
                if (len(phone_number) == 10):
                    if (phone_number.isdigit()):
                        self.contact[name] = phone_number
                        print("Phone number successfully saved")
                        break
                    else:
                        print("Phone number should not contain charector!!")
                else:
                    print("Phone number should contain 10 digit")
        else:
            print("Battery is running low. Please charge it")


    # Displays all contacts stored in the contact book
    def view_contact(self):
        if (self.battery > 20):
            if (not self.contact):
                print("Contact is empty")
            else:
                print("Contacts :")
                for key,value in self.contact.items():
                    print(key, ":",value)
        else:
            print("Battery is running low. Please charge it")

    # Method to delete a saved contact from the contact book
    def delete_contact(self):
        if (self.battery > 20):
            if (not self.contact):
                print("Contact is empty")
            else:
                contact_name = input("Enter the contact name to delete :")
                if (contact_name in self.contact):
                    del self.contact[contact_name]
                    print("Contact deleted successfully!")
                else:
                    print("Contact not found!!")
        else:
            print("Battery is running low. Please charge it")

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
print("6.Show message history")
print("7.Show phone battery")
print("8.Charge battery")
print("9.See menu")
print("10.Add Contact")
print("11.View saved contact")
print("12.Delete contact")
print("13.Exit")

# Processing user's menu choice
while True:


    choice=int(input("Enter a choice number from the menu : "))

    if phone1.battery>20:
        if choice==1:
            phone1.showdetails()
        elif choice==2:
            phone1.call()
        elif choice==3:
            phone1.message()
        elif choice==4:
            phone1.playmusic()
        elif choice==5:
            print(phone1.call_list) 
        elif choice==6:
            if not phone1.message_list:
                print("History is empty")
            else:    
                print(phone1.message_list)
        elif choice==7:
            print(phone1.battery)
        elif choice==8:
            phone1.charge_phone()
        elif choice == 9:
            phone1.see_menu()  
        elif choice == 10:
            phone1.add_contact() 
        elif choice == 11:
            phone1.view_contact()  
        elif choice == 12:
            phone1.delete_contact()           
        elif choice == 13:
            exit()    
        else:
            print("Please enter a valid number!!!")                    
    else:
        print("Battery running slow please charge it./n current battery :  ",phone1.battery)
        exit()

