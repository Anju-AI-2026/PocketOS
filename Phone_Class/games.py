# Game manager class to provide entertainment features

import random

class GameManager:

    # Constructor to initialize the battery manager
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager

    # Method to see the game menu
    def see_game_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                    🎮 GAME CENTER                    ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. ✊ Rock Paper Scissors                           ║")
        print("║  2. 🍀 Lucky Fortune                                 ║")
        print("║  3. 🔤 Hangman                                       ║")
        print("║  4. 📋 Show Menu                                     ║")
        print("║  5. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")

    # Method to create the rock, paper, scissors game
    def rock_paper_scissors(self):
        self.battery_manager.consume_battery(5)

        emojis = {'r': '👊', 's': '✂️', 'p': '📃'}
        choice = ('r', 'p', 's')

        print("\n" + "═"*13 + " ✊ ROCK • PAPER • SCISSORS ✂️ " + "═"*13 + "\n")

        while True:
            user_choice = input("🎯 Choose Rock, Paper or Scissors (r/p/s): ").lower()

            if user_choice not in choice:
                print("\n❌ Invalid choice. Please enter r, p, or s.\n")
                continue

            computer_choice = random.choice(choice)

            print(f"\n🙋 You chose      : {emojis[user_choice]}")
            print(f"🤖 Computer chose : {emojis[computer_choice]}\n")

            if (user_choice == computer_choice):
                print("🤝 It's a tie!")

            elif (
                (user_choice == 'r' and computer_choice == 's') or
                (user_choice == 's' and computer_choice == 'p') or
                (user_choice == 'p' and computer_choice == 'r')
            ):
                print("🎉 Congratulations! You won!")
                self.battery_manager.consume_battery(2)

            else:
                print("😔 You lost. Better luck next time!")

            while True:
                should_continue = input("\n🔄 Play another round? (y/n): ").lower()

                if should_continue == 'y':
                    print()
                    break

                elif should_continue == 'n':
                    return

                else:
                    print("\n❌ Please enter a valid choice (y/n).\n")

    # Method to create the Lucky Fortune
    def lucky_fortune(self):
        self.battery_manager.consume_battery(5)

        print("╔" + "═"*54 + "╗")
        print("║                  🍀 LUCKY FORTUNE                    ║")
        print("╚" + "═"*54 + "╝\n")

        # List of personalities
        lucky_personalities = [
            "Leader",
            "Creative",
            "Kind",
            "Brave",
            "Wise",
            "Hardworking",
            "Friendly",
            "Adventurous",
            "Confident",
            "Optimistic"
            ]

        # List of colours
        lucky_colors = [
            "Red",
            "Blue",
            "Green",
            "Yellow",
            "Purple",
            "Pink",
            "Orange",
            "Black",
            "White",
            "Silver"
            ]

        # List of foods
        lucky_foods = [
            "Pizza",
            "Burger",
            "Ice Cream",
            "Chocolate",
            "Biryani",
            "Pasta",
            "Momos",
            "Dosa",
            "Sandwich",
            "Cake"
            ]

        # List of moods
        lucky_moods = [
            "Happy",
            "Calm",
            "Confident",
            "Excited",
            "Relaxed",
            "Energetic",
            "Focused",
            "Creative",
            "Hopeful",
            "Cheerful"
            ]

        # List of activities
        lucky_activities = [
            "Study something new",
            "Practice coding",
            "Read a book",
            "Go for a walk",
            "Exercise",
            "Listen to music",
            "Watch a movie",
            "Draw something",
            "Spend time with family",
            "Call a friend"
            ]

        # List of quotes
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

            user_choice = input("🎲 Enter your lucky number (0-100): ")

            if (user_choice.isdigit()):
                user_choice = int(user_choice)

                if (user_choice >= 0 and user_choice <= 100):

                    random_personalities = random.choice(lucky_personalities)
                    random_colours = random.choice(lucky_colors)
                    random_foods = random.choice(lucky_foods)
                    random_moods = random.choice(lucky_moods)
                    random_activities = random.choice(lucky_activities)
                    random_quotes = random.choice(lucky_quotes)

                    print("\n" + "═"*20 + " 🌟 YOUR LUCKY FORTUNE 🌟 " + "═"*20)
                    print(f"\n🎲 Lucky Number      : {user_choice}")
                    print(f"✨ Personality       : {random_personalities}")
                    print(f"🎨 Lucky Colour      : {random_colours}")
                    print(f"🍜 Lucky Food        : {random_foods}")
                    print(f"😊 Lucky Mood        : {random_moods}")
                    print(f"🎯 Lucky Activity    : {random_activities}")
                    print(f"💭 Lucky Quote       : {random_quotes}")
                    print("\n" + "═"*60)

                    self.battery_manager.consume_battery(5)
                    break

                else:
                    print("\n❌ Please enter a number between 0 and 100.\n")

            else:
                print("\n❌ Invalid input. Enter a number between 0 and 100.\n")

        while True:
            should_continue = input("\n🔄 Try another lucky fortune? (y/n): ").lower()

            if should_continue == 'y':
                break

            elif should_continue == 'n':
                return

            else:
                print("\n❌ Please enter a valid choice (y/n).\n")

    # Method to develop the hangman game
    def hangman_game(self):
        print("╔" + "═"*54 + "╗")
        print("║                    🔤 HANGMAN GAME                   ║")
        print("╚" + "═"*54 + "╝\n")

        words = [
            "apple", "python", "mobile", "friend", "coffee",
            "camera", "laptop", "music", "coding", "future"
        ]

        while True:

            random_word = random.choice(words)
            reference_list = ["_"] * len(random_word)
            guessed_word = []
            lives = 6

            while True:

                print("═" * 35)
                print(f"❤️ Lives : {'❤️  ' * lives}\n")

                print("🔤 WORD")
                print(" ".join(reference_list))
                print()

                print("📝 GUESSED LETTERS")
                if guessed_word:
                    print(" ".join(guessed_word))
                else:
                    print("None")
                print()

                user_guess = input("🔠 Enter a letter: ").lower()

                # Validation
                if not user_guess.isalpha():
                    print("\n❌ The guess should be a letter.\n")
                    continue

                if len(user_guess) != 1:
                    print("\n❌ Enter only one letter.\n")
                    continue

                if user_guess in guessed_word:
                    print("\n❌ This letter has already been guessed.\n")
                    continue

                guessed_word.append(user_guess)

                # Correct Guess
                if user_guess in random_word:
                    for i in range(len(random_word)):
                        if random_word[i] == user_guess:
                            reference_list[i] = user_guess
                else:
                    print("\n❌ Wrong guess!")
                    lives -= 1

                # Win
                if "_" not in reference_list:
                    print("\n🎉 Congratulations!")
                    print(f"🏆 You guessed the word: {random_word.upper()}")
                    break

                # Lose
                if lives == 0:
                    print("\n💀 Game Over!")
                    print(f"📖 Correct Word: {random_word.upper()}")
                    break

            while True:
                should_continue = input("\n🔄 Play again? (y/n): ").lower()

                if should_continue == "y":
                    break
                elif should_continue == "n":
                    return
                else:
                    print("\n❌ Please enter a valid choice (y/n).\n")

    # Method to demonstate the game app
    def game_manager(self):
        if not self.battery_manager.check_battery():
            return

        self.see_game_menu()

        while True:
            print("\n" + "─"*42)
            print("🎮 What would you like to play?")
            print("─"*42)

            choice = input("\n➡️  Enter your choice: ")

            if (choice.isdigit()):
                choice = int(choice)

                if (choice == 1):
                    self.rock_paper_scissors()

                elif (choice == 2):
                    self.lucky_fortune()

                elif (choice == 3):
                    self.hangman_game()

                elif (choice == 4):
                    self.see_game_menu()

                elif (choice == 5):
                    return

                else:
                    print("\n❌ Please enter a valid menu choice.\n")

            else:
                print("\n❌ Error: Choice must be a digit.\n")
