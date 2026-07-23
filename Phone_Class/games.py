import random 

class GameManager:

    # Method to see the game menu
    def see_game_menu(self):
        print("="*35)
        print("             GAME MENU")
        print("="*35)
        print("1.Rock Paper Scissors")
        print("2.Lucky Fortune")
        print("3.Hangnam")
        print("4.Tic Tac Toe")
        print("5.See menu")
        print("6.Back")

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

  # Method to demonstate the game app
    def game_manager(self):
        self.see_game_menu()

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
                        self.see_game_menu()

                    elif choice == 6 :
                        return

                    else:
                        print("Enter a valid choice from yhe menu")    
                else:
                    print("Choice should be a number ")
