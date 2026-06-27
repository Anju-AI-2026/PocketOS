# Program to demonstrate a phone class 

class Phone:

    # Constructor to initialize phone details and default values
    def __init__(self,name,brand,colour,memory):
        self.name=name
        self.brand=brand
        self.colour=colour
        self.memory=memory
        self.list=[]
        self.list1=[]
        self.battery=100

    # Method to display phone details
    def showdetails(self):
        print("Mobile Phone company name :",self.name)
        print("The mobile phone brand is : ",self.brand)
        print("The colour of the mobile phone",self.colour)
        print("The memory of the mobile phone is : ",self.memory)

    # Method to make a phone call and store call history
    def call(self):
        if self.battery>20:
            num=(input("Enter the phone number : +19"))    
            if (len(num)==10):
                print("Dialing!!!!!")
                self.list.append(num)
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
                self.list1.append((num,msg))
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
            print("Playing",music,"music")
            if self.battery>0:
                self.battery=self.battery-15
        else:
            print("Battery is running low. Please charge it")

#Password authentication before accessing the phone
real_p=12345   
password=int(input("Enter the password : "))
if(real_p==password):
    print("The password is correct")
else:
    print("The password is incorrect")   
    exit() 

#Taking phone details from the user
name=input("Enter the phone company name : ")
brand=input("Enter the mobile phone brand name : ")
colour=input("Enter the mobile phone colour : ")
memory=input("Enter the memory of the mobile phone : ")

#Creating a Phone object
phone1=Phone(name,brand,colour,memory)


#Displaying menu repeatedly until the user exits the program
while True:
    print("========Menu========")
    print("1.Show the details of the Mobile phone")
    print("2.Make a call")
    print("3.Send a message")
    print("4.Play a music") 
    print("5.Show call history")
    print("6.Show message history")
    print("7.Show phone battery")
    print("8.Exit")

    #Processing user's menu choice
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
            print(phone1.list) 
        elif choice==6:
            if not phone1.list1:
                print("History is empty")
            else:    
                print(phone1.list1)
        elif choice==7:
            print(phone1.battery)
        elif choice == 8:
            exit()    
        else:
            print("Please enter a valid number!!!")                    
    else:
        print("Battery running low please charge it.\nCurrent battery :", phone1.battery)
        exit()
