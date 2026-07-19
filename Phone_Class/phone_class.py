from contacts import ContactManager
from calls import CallManager
from messages import MessageManager
from calculator import CalculatorManager
import random

# Program to demonstrate a phone class 

class Phone(ContactManager, CallManager, MessageManager, CalculatorManager):

     # Constructor to initialize phone details and default values
    def __init__(self,name,brand,colour,memory):

        ContactManager.__init__(self)
        CallManager.__init__(self)
        MessageManager.__init__(self)
        CalculatorManager.__init__(self) 
         
        self.name = name
        self.brand = brand
        self.colour = colour
        self.memory = memory
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
        print("15.Delete Call history")
        print("16.Clear call history")
        print("17.Clear message history") 
        print("18.Calculator")  
        print("19.Games") 
        print("20.Exit") 

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
