from contacts import ContactManager
from calls import CallManager
from messages import MessageManager
from calculator import CalculatorManager
from music import MusicManager
import random

# Program to demonstrate a phone class 

class Phone(ContactManager, CallManager, MessageManager, CalculatorManager, MusicManager):

     # Constructor to initialize phone details and default values
    def __init__(self,name,brand,colour,memory):

        ContactManager.__init__(self)
        CallManager.__init__(self)
        MessageManager.__init__(self)
        CalculatorManager.__init__(self) 
        MusicManager.__init__(self)
         
        self.name = name
        self.brand = brand
        self.colour = colour
        self.memory = memory
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
