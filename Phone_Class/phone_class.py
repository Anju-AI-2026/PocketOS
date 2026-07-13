import random

# Program to demonstrate a phone class 

class Phone:

     # Constructor to initialize phone details and default values
    def __init__(self,name,brand,colour,memory):
        self.name = name
        self.brand = brand
        self.colour = colour
        self.memory = memory
        self.call_list = []
        self.message_list = []
        self.contact = {}
        self.play_list = {}  
        self.battery=100

    # Method to display phone details
    def showdetails(self):
        self.battery=self.battery-2
        print("Mobile Phone company name :",self.name)
        print("The mobile phone brand i : ",self.brand)
        print("The colour of the mobile phone",self.colour)
        print("The memory of the mobile phone is : ",self.memory)

    # Method to see the menu
    def see_menu(self):
        print("========Menu========")
        print("1.Show the details of the Mobile phone")
        print("2.Make a call")
        print("3.Send a message")
        print("4.Music app")
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

    # Adds a contact after validating the name and phone number
    def add_contact(self):
        self.battery=self.battery-2
        while True:
            name=input("Enter the contact name :")
            if (name in self.contact):
                print("Contact already exit")
                return
            else:
                if (name.replace(" ","").isalnum()):
                    if (name.isdigit()):
                        print("Contact name should not be only made up of numbers!")
                    else:
                        break
                else:
                    print("Name only contain alphabet or alphanumeric name")

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

    # Displays all contacts stored in the contact book
    def view_contact(self):
        self.battery=self.battery-2
        if (not self.contact):
            print("=================")
            print("Contact is empty")
            print("=================")
        else:
            print()
            print("==========CONTACT BOOK==========")
            print()
            print("\nContacts :")
            count = 1
            for key,value in self.contact.items():
                    print(count)
                    print("Name :",key)
                    print("Number :",value) 
                    print("-" * 20)  
                    count=count+1

    # Method to display call history
    def view_call_history(self):
        self.battery = self.battery - 2

        if not self.call_list:
            print("==========================")
            print("No call history available.")
            print("==========================")
            return

        print("\n========== CALL HISTORY ==========\n")

        for index, call in enumerate(self.call_list, start=1):
            print(f"Call {index}")
            print(f"Name   : {call['name']}")
            print(f"Number : {call['number']}")
            print(f"Type   : {call['type']}")
            print("-" * 35)
            
    # Method to delete the contact from the contact
    def delete_contact(self):
        self.battery=self.battery-2
        if (not self.contact):
            print("Contact is empty")
        else:
            while True:
                contact_name = input("Enter the contact name to delete :")
                if (contact_name.isalnum()):
                    if (contact_name in self.contact):
                        del self.contact[contact_name]
                        print("Contact deleted successfully!")
                        break 
                else:
                    print("Contact not found")         

    # Method to search for contact in recent call and contact also
    def search_contact(self):
        search_record = input("Enter the name or number to search :") 
        found = False
        if (search_record.isdigit()):
            for key,value in self.contact.items():
                if (search_record == value):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :{key}")
                    print(f"Number : {value}")
                    print("="*20)
                    return
            for call in self.call_list:
                if (search_record == call["number"]):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :",call["name"])
                    print(f"Number :",call["number"])
                    print("="*20)
                    return

        else:
            for key, value in self.contact.items():
                if (search_record == key):
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :{search_record}")                        
                    print(f"Number : {self.contact[search_record]}")
                    print("="*20)
                    return 
            for call in self.call_list:
                if (search_record == call["name"]) :
                    print("="*20)
                    print("Search sucssefull!!")
                    print(f"Name :",call["name"])
                    print(f"Number :",call["number"])
                    print("="*20)
                    return

        if not found:
            print("====================")
            print("Contact not found")
            print("====================")
        


    # Method to make a phone call and store call history
    def call(self):
        user_choice=(input("Enter the contact number or name:")) 
        if (user_choice.isdigit()):   
            if (len(user_choice)==10):
                    for key,value in self.contact.items():
                        if (value == user_choice):
                            print(f"Calling {key}")
                            print("Dialing!!!!!")
                            call_record = {
                                "name" : key ,
                                "number" : value,
                                "type" : "Outgoing" 
                            }
                            self.call_list.append(call_record)
                            self.battery=self.battery-10
                            return
                    while True:
                        save_choice = input("Do you want to save the number? (y/n) :").lower()
                        if (save_choice.isalpha()):
                            if save_choice == "y":
                                while True:
                                    name=input("Enter the contact name :")
                                    if (name.replace(" ","").isalnum()):
                                        if (name.isdigit()):
                                            print("Contact name should not be only made up of numbers!")
                                        else:
                                            call_record = {
                                                "name" : name,
                                                "number" : user_choice,
                                                "type" : "Outgoing"
                                            }
                                            self.call_list.append(call_record)
                                            self.contact[name] = user_choice
                                            self.battery=self.battery-10
                                            print("Contact saved successfully!")
                                            print(f"Calling {name}")
                                            print("Dialing!!!")
                                            return 
                                    else:
                                        print("Name only contain alphabet or alphanumeric name")       
                            elif (save_choice == "n"):
                                print("Calling unknown number")
                                print("Dialing!!!!!")  
                                call_record = {
                                    "name" : "Unknown",
                                    "number" : user_choice,
                                    "type" : "Outgoing"
                                }
                                self.call_list.append(call_record)
                                self.battery=self.battery-10
                                return
                            else:
                                print("Please enter a valid choice!")
                        else:
                            print("Please enter a valid choice")
            else:   
                print("Please enter a 10 digit number")
        else:
            if (user_choice in self.contact):
                print(f"Calling {user_choice}")
                print("Dialing!!!!!")
                call_record={
                    "name" : user_choice,
                    "number" : self.contact[user_choice],
                    "type" : "Outgoing" 
                }
                self.call_list.append(call_record)
                self.battery=self.battery-10
                return
            else:
                print("Contact not found")

     # Method to delete a call history
    def delete_call_history(self):
        if (not self.call_list):
            print("The call history is empty can not delete")
            return
        else:
            for index, call in enumerate(self.call_list, start=1):
                print(f"Call {index}")
                print(f"Name   : {call['name']}")
                print(f"Number : {call['number']}")
                print(f"Type   : {call['type']}")
                print("-" * 35) 
            while True:
                choice = input("Enter the call number to delete::")
                if (choice.isdigit()):
                    choice = int(choice) 
                    length = len(self.call_list)
                    if (choice >= 1 and choice <= length):
                        del self.call_list[choice-1]
                        return
                    else:
                        print("Choice is out of range")


 # Method to display call history
    def view_message_history(self):
        self.battery = self.battery - 2

        if not self.message_list:
            print("==========================")
            print("No message history available.")
            print("==========================")
            return

        print("\n========== MESSAGE HISTORY ==========\n")

        for index, message in enumerate(self.message_list, start=1):
            print(f"Message {index}")
            print(f"Name   : {message['name']}")
            print(f"Number : {message['number']}")
            print(f"Messgae : {message['message']}")
            print(f"Type   : {message['type']}")
            print("-" * 35)

    # Method to delete a individual message from history
    def delete_message(self):
        self.battery=self.battery-2
        if (not self.message_list):
            print("Message history is empty")
        else:
            while True:
                contact_name = input("Enter the contact name to delete :")
                if (contact_name.isalnum()):
                    for i, message in enumerate(self.message_list):
                        if contact_name == message["name"]:
                            del self.message_list[i]
                            print("Message deleted successfully!")
                            return
            else:
                print("Message not found") 


    # Method to send messages and store message history
    def message(self):
        user_choice=(input("Enter the phone number or name to send message : "))
        if (user_choice.isdigit()):
            if (len(user_choice)==10):
                for key,value in self.contact.items():
                    if (value == user_choice):
                        msg=input(f"Enter the message to send {key} : ")    
                        message_chat={
                            "name" : key,
                            "number" : value,
                            "message" : msg,
                            "type" : "Sent"
                        }
                        print("Message sent!!!")
                        self.message_list.append(message_chat)
                        self.battery=self.battery-5
                        return
                while True:
                    save_choice=input("Do you want to save the number? (y/n) :").lower()
                    if (save_choice.isalpha()):
                        if save_choice == "y":
                    
                            while True:
                                name = input("Enter the name to save contact :")
                                if (name.replace(" ","").isalnum()):
                                    if(name.isdigit()):
                                        print("Name should not be only made up of number :")
                                    else:
                                        msg=input("Enter the message to send :")
                                        message_chat={
                                            "name" : name,
                                            "number" : user_choice,
                                            "message" : msg,
                                            "type" : "Sent"
                                        }  
                                        print("Message sent!!!")
                                        self.message_list.append(message_chat) 
                                        self.contact[name] = user_choice
                                        self.battery=self.battery-5
                                        return
                                else:
                                    print("Name only contain alphanumeric ")    
                        elif (save_choice == "n"):
                            msg=input("Enter the message to send unknown number :")
                            message_chat= {
                                "name" : "Unknown",
                                "number" : user_choice,
                                "message" : msg,
                                "type" : "Sent"
                            }  
                            print("Message sent!!!")
                            self.message_list.append(message_chat) 
                            self.battery=self.battery-5
                            return
                        else:
                            print("Please enter a valid choice!")
                    else:
                        print("Please enter a valid choice!")        
        else:
            if(user_choice in self.contact):
                msg=input(f"Enter the message to send {user_choice}: ")
                message_chat= {
                    "name" : user_choice,
                    "number" : self.contact[user_choice],
                    "message" : msg,
                    "type" : "Sent"
                }  
                print("Message sent!!!")
                self.message_list.append(message_chat) 
                self.battery=self.battery-5
                return
            else:
                print("Contact not found") 

    
    # Method to play music and reduce battery percentage
    def music_app(self):
        print("1.Play music")
        print("2.Show play list")
        print("3.Add song")
        print("4.Delete song")
        print("5.Stop music")
        print("6.Back")

        while True :
            choice = input("Enter a choice from the above menu :")

            if (choice.isdigit()):
                choice = int(choice)
                if choice == 1:
                    self.play_music()
                elif choice == 2:
                    self.show_play_list()
                elif choice == 3:
                    self.add_song()
                elif choice == 4:
                    self.delete_song()
                elif choice == 5:
                    self.stop_song()
                elif choice == 6:
                    break
                else:
                    print("Enter a valid choice from the menu ")
            else:
                print("Choice should be a number")   

     # Method to show the playlist
     def show_play_list(self):
        self.play_list = {
            1 : "Perfect",
            2 : "Love me like you do",
            3 : "Living hell",
            4 : "Unholy"
        }
        print("="*25)
        print("           PLAY LIST           ")
        print("="*25)

        if (not self.play_list):
            print("The playlist is empty")
        else:
            for key,value in self.play_list.items():
                print(key,". " ,value)

     # Method to play a music
    def play_music(self):
        if (not self.play_list):
            print("The play list is empty")
        else:
            print("="*25)
            print("           PLAY LIST           ")
            print("="*25)
            for key,value in self.play_list.items():
                print(key,". " ,value)

            while True :
                choice = input("Enter any song number from the playlist")

                if (choice.isdigit()):
                    choice = int(choice)
                    if choice in self.play_list :
                        self.current_song = self.play_list[choice]
                        print(f" 🎶 Now playing {self.current_song}")
                        return
                    else:    
                        print("Error : Song number not found")
                else:
                    print("The choice should be a number")            

     # Method to add a new song to the play list
    def add_song(self):
        while True:

            song_name = input("Enter the song name to add to the play list :")
            if (song_name.replace(" ","" ).isalnum()):

                if (not self.play_list):  
                    self.play_list[1] = song_name
                    print("Song added successfully !!")
                    return
                elif (song_name in self.play_list.values()):
                    print("Song already exits")    
                else:
                    current_number = max(self.play_list)
                    self.play_list[current_number+1] = song_name
                    print("Song added successfully!!")
                    return
            else:
                print("The song should contain only alphanumeric name")    

     # Method to reorganize the playlist
    def reorganize_playlist(self):
        new_play_list ={}
        if (not self.play_list):
            return False
        else:
            for number ,value in enumerate(self.play_list.values(), start = 1):
                new_play_list[number] = value

            self.play_list = new_play_list
            return    

     # Method to delete a song from the play list
    def delete_song(self):
        if (not self.play_list):
            print("The play list is empty can not delete")
        else:
            print("="*25)
            print("           PLAY LIST           ")
            print("="*25)
            for key,value in self.play_list.items():
                print(key,". " ,value)

            while True :
                choice = input("Enter any song number from the playlist")

                if (choice.isdigit()):
                    choice = int(choice)
                    if (choice in self.play_list):
                        if (self.play_list[choice] == self.current_song):
                            stop_music = input("Do you want to delete the current playing music (y/n) :").lower()
                            if (stop_music == "y"):
                                del self.play_list[choice]
                                self.current_song = None
                                print("🎶 Music stopped ")
                                print("🗑️ Song deleted successfully.")
                                self.reorganize_playlist()
                                return
                            elif (stop_music == "n"):
                                break
                            else:
                                print("Invalid choice")
                        else:
                            del self.play_list[choice]
                            print("🗑️ Song deleted successfully.")
                            self.reorganize_playlist()
                            return
                            
                    else:
                        print("The choice is not in playlist")                       
                else:
                    print("Invalid choice") 

     # Method to stop the song
    def stop_song(self):
        if self.current_song is None :
            print("No music is playing.")
            return
        else:
            self.current_song = None
            print("Music stopped successfully.")    

     
    # Method to show calculator menu
    def calculator_menu(self):
        print("====================")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Find Square")
        print("7.Find Cube")
        print("8.See calculator menu")
        print("9.Back")
       
    # Method to take user choice for calculator
    def calculator(self):
        print("====================")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Find Square")
        print("7.Find Cube")
        print("8.See calculator menu")
        print("9.Back")
        if (self.battery <=20):
            print("Battery is low please charge it")
            return
        else:
            while True :
                choice = input("Enter the choice from above menu :")
                if choice.isdigit():
                    choice = int(choice)
                    if (choice == 1):
                        self.addition()
                    elif (choice == 2):
                        self.subtraction()
                    elif (choice == 3):
                        self.multiplication()
                    elif (choice == 4):
                        self.division()
                    elif (choice == 5):
                        self.modulus()
                    elif (choice == 6):
                        self.square()
                    elif (choice == 7):
                        self.cube()
                    elif (choice == 8):
                        self.calculator_menu()    
                    elif (choice == 9):
                        return
                    else:
                        print("Please enter a valid choice") 
                else:
                    print("Error : choice should be a digit")                                     

    # Method to calculate the summation of numbers
    def addition(self):
        numbers = []
        while True :
            num = input("Enter the limit to the numbers:")
            if (num.isdigit()):
                num = int(num)
                for i in range(1,num+1):
                    while True:
                        x=input(f"Enter the {i} numbers:")
                        if (x.isdigit()):
                            x = int(x)
                            numbers.append(x)
                            break
                        else:
                            print("Invalid input!! Enter again")     
                total = sum(numbers)
                print("The sum of all number is :",total)
                self.battery = self.battery - 2
                return
            else:
                print("The limit should be a number.")

    # Method to calculate the multiplication of numbers
    def multiplication(self):
        numbers = []
        total = 1
        while True :
            num = input ("Enter the limit to the numbers :")
            if (num.isdigit()):
                num = int(num)
                for i in range(1,num+1):
                    while True:
                        x = input(f"Enter the {i} numbers :")
                        if (x.isdigit()):
                            x = int(x)
                            numbers.append(x)
                            break
                        else:
                            print("Invalid Input!! Enter again")
                for number in numbers:
                    total = total * number          
                print("The multiplication of all number is :",total)
                self.battery = self.battery - 2
                return
            else:
                print("The limit should be a number")    
    
    # Method to calculate the subtraction of numbers
    def subtraction(self):
        while True:
            numbers = []
            while True :
                num = input("Enter the limit to the numbers :")
                if(num.isdigit()):
                    num = int(num)
                    for i in range(1,num+1):
                        while True:
                            x = input(f"Enter the {i} numbers :")
                            if (x.isdigit()):
                                x = int(x)
                                numbers.append(x)
                                break
                            else:
                                print("Invalid Input!! Enter again")
                total = numbers[0]                
                for j in range (1,len(numbers)):
                    total = total - numbers[j]
                print("The subtraction of numbers is :", total)     
                self.battery = self.battery - 2
                return
            else:
                print("The limit should be a number")               

    # Method to calculate the division of numbers
    def division(self):
        while True:
            num1=input("Enter the first number :")
            if(num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("Number should be a digit")
        while True:
            num2 = input("Enter the second number :")
            if(num2.isdigit()):
                num2=int(num2)
                if (num2 != 0):
                    print("The division of numbers is :" ,(num1 / num2) )
                    self.battery = self.battery - 2
                    return
                else:
                    print("Error : Cannot divide by zero.")
            else:
                print("Number should be a digit")

    # Method to find the remainder of numbers
    def modulus(self):
        while True:
            num1=input("Enter the first number :")
            if(num1.isdigit()):
                num1 = int(num1)
                break
            else:
                print("Number should be a digit")
        while True:
            num2 = input("Enter the second number :")
            if(num2.isdigit()):
                num2=int(num2)
                if (num2 != 0):
                    print("The Remainder is :" ,(num1 % num2) )
                    self.battery = self.battery - 2
                    return
                else:
                    print("Error : Number can not be zero.")
            else:
                print("Number should be a digit")            

    # Method to find the square of a number
    def square(self):
        while True:
            number = input("Enter the number to find square :")
            if (number.isdigit()):
                number = int(number)
                print(f"The square of the {number} is :", (number*number))
                self.battery = self.battery - 2
                return
            else:
                print("Number should be a digit")           

    # Method to find the cube of a number
    def cube(self):
        while True:
            number = input("Enter the number to find cube :")
            if (number.isdigit()):
                number = int(number)
                print(f"The cube of the {number} is :", (number*number*number))
                self.battery = self.battery - 2
                return
            else:
                print("Number should be a digit")           
            
  # Method to demonstate the game app
    def games(self):
        print("1. Rock Paper Scissors")
        print("2.Lucky Fortune")
        print("3.Hangnam")
        print("4.Tic Tac Toe")
        print("5.Back")

        if (self.battery <= 20):
            print("The battery is low please charge it")
            return
        else:
            while True:
                choice = input("Enter a choice from the menu :")
                if (choice.isdigit()):
                    choice = int(choice)

                    if (choice == 1):
                        self.rock_paper_scissors()

                    elif (choice == 2):
                        self.lucky_fortune()

                    elif (choice == 3):
                        print("Still in development level")

                    elif (choice == 4):
                        print("Still in development level")

                    elif (choice == 5):
                        return

                    else:
                        print("Enter a valid choice from yhe menu")    
                else:
                    print("Choice should be a number ")

        
    # Method to create the rock, paper, scissors game
    def rock_paper_scissors(self):

        emojis = {'r' : '👊' , 's' : '✂️' , 'p' : '📃'}
        choice= ('r' , 'p' , 's')

        while True:
            user_choice = input("Rock, Paper, Scissors? (r/p/s) :").lower()
            if user_choice not in choice:
                print("Invalid choice!")
                continue

            computer_choice = random.choice(choice) 

            print(f"You chose {emojis[user_choice]}")
            print(f"Computer chose {emojis[computer_choice]}")  

            if  (user_choice == computer_choice) :
                print("Tie!")
            elif (
                (user_choice == 'r' and computer_choice == 's')or
                (user_choice == 's' and computer_choice == 'p') or
                (user_choice == 'p' and computer_choice == 'r')):
                print("You won!")
            else:
                print("You lose!")        

            while True:
                should_continue = input("Continue? (y/n) :").lower()
                if should_continue == 'y':
                    break
                elif should_continue == 'n':
                    return
                else:
                    print("Invalid choice!")

         # Method to create the Lucky Fortune
    def lucky_fortune(self):
        print("="*30)
        print("          LUCKY FORTUNE          ")
        print("="*30)
        lucky_personalities = ["Leader","Creative","Kind","Brave", "Wise","Hardworking","Friendly","Adventurous","Confident","Optimistic"]
         
        lucky_colors = ["Red","Blue","Green","Yellow","Purple","Pink","Orange","Black","White","Silver"]
         
        lucky_foods = ["Pizza","Burger","Ice Cream","Chocolate","Biryani","Pasta","Momos","Dosa","Sandwich","Cake"]
         
        lucky_moods = [ "Happy","Calm","Confident","Excited","Relaxed","Energetic","Focused","Creative","Hopeful","Cheerful"]
         
        lucky_activities = [ "Study something new","Practice coding","Read a book","Go for a walk","Exercise","Listen to music","Watch a movie","Draw something","Spend time with family","Call a friend"]
         
        lucky_quotes = [
    "Believe in yourself.",
    "Every day is a new beginning.",
    "Dream big and work hard.",
    "Small steps lead to big success.",
    "Stay positive and keep smiling.",
    "Your effort will never be wasted.",
    "Today's challenge is tomorrow's strength.",
    "Great things take time.",
    "Be fearless in chasing your dreams.",
    "Success starts with consistency."
]
        while True:

            user_choice = input("Enter your lucky number from (0 to 100) :")
            if (user_choice.isdigit()):
                user_choice = int(user_choice)
                if (user_choice >= 0 and user_choice <= 100 ):
                    random_personalities = random.choice(lucky_personalities)
                    random_colours = random.choice(lucky_colors)
                    random_foods = random.choice(lucky_foods)
                    random_moods = random.choice(lucky_moods)
                    random_activities = random.choice(lucky_activities)
                    random_quotes = random.choice(lucky_quotes)

                    print("🎲 Lucky number :",user_choice)
                    print()
                    print("✨ Lucky Personality :", random_personalities)
                    print("🎨 Lucky Colour :", random_colours)
                    print("🍜 Lucky Food :", random_foods)
                    print("😊 Lucky Mood :", random_moods)
                    print("🎯 Lucky Activity :", random_activities)
                    print("💭 Lucky Quote :", random_quotes)
                    break
                else:
                    print("Number should be between o to 100")
            else:
                print("Enter the number from 0 to 100 onlt !!!")  

        while True:
            should_continue = input("Continue? (y/n) :").lower()
            if should_continue == 'y':
                break
            elif should_continue == 'n':
                return
            else:
                print("Invalid choice!")

     # Still at development stage
     # Method to develop the hangnam game
    def hangman_game(self):
        print("="*25)
        print("          Hangnam Game           ")
        print("="*25)
        words = ["apple","python","mobile","friend","coffee","camera","laptop","music","coding","future"]
        random_word = random.choice(words)
        reference_list = ["_"]*len(random_word)
        lives = 6 
        guessed_word = []
        while True :
            print("="*10)
            print("❤️"*lives)
            print("GUESSED WORD :")
            print(reference_list)
            while True :
                user_guess = input("Enter a letter :")
                while True :
                    if (user_guess.isalpha()):  
                        if (user_guess in guessed_word):
                            print("The letter is already guessed")
                            break
                        else:     
                            if user_guess in random_word:
                                for i in range(len(random_word)):
                                    if user_guess == random_word[i] :
                                        guessed_word.append(user_guess)
                                        reference_list[i] = user_guess
                            else:
                                print("Guess again ")
                                lives -=1             
                    else:
                        print("The guess should be a letter ")                
            if ("_" in reference_list):   
                continue 
            else:
                print("You won !!")
                break 

        while True:
            should_continue = input("Continue? (y/n) :").lower()
            if should_continue == 'y':
                break
            elif should_continue == 'n':
                return
            else:
                print("Invalid choice!")    
