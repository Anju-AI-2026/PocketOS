# Music manager class to handle playlist and music playback

from storage import save_music, load_music

class MusicManager:

    # Constructor to initialize playlist and current song
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager

        music_data = load_music()

        self.play_list = music_data["playlist"]
        self.current_song = music_data["current_song"]

    # Method to see the music menu
    def see_music_menu(self):
        print("╔" + "═"*54 + "╗")
        print("║                   🎵 MUSIC PLAYER                    ║")
        print("╠" + "═"*54 + "╣")
        print("║  1. ▶️  Play Music                                    ║")
        print("║  2. 🎼 Show Playlist                                 ║")
        print("║  3. ➕ Add Song                                      ║")
        print("║  4. 🗑️  Delete Song                                   ║")
        print("║  5. ⏹️  Stop Music                                    ║")
        print("║  6. 📋 Show Menu                                     ║")
        print("║  7. 🔙 Back                                          ║")
        print("╚" + "═"*54 + "╝\n")

    # Method to show the playlist
    def show_play_list(self):

        print("\n" + "═"*16 + " 🎼 PLAYLIST " + "═"*16 + "\n")

        # Display stored records
        if not self.play_list:
            print("📭 Playlist is empty.\n")
        else:
            for key, value in self.play_list.items():
                print(f"🎵 {key}. {value}")

            self.battery_manager.consume_battery(2)
            save_battery(self.battery_manager.battery)

    # Method to play music
    def play_music(self):
        if (not self.play_list):
            print("\n📭 Playlist is empty.\n")
        else:
            print("\n" + "═"*16 + " 🎼 PLAYLIST " + "═"*16 + "\n")

            for key, value in self.play_list.items():
                print(f"🎵 {key}. {value}")

            while True:
                choice = input("\n▶️ Enter a song number from the playlist: ")

                if (choice.isdigit()):
                    choice = int(choice)

                    if choice in self.play_list:
                        self.current_song = self.play_list[choice]
                        save_music(self.play_list, self.current_song)

                        print(f"\n🎶 Now Playing: {self.current_song}\n")

                        self.battery_manager.consume_battery(7)
                        return
                    else:
                        print("\n❌ Song number not found.\n")
                else:
                    print("\n❌ Choice should be a number.\n")

    # Method to add a new song to the playlist
    def add_song(self):
        while True:

            song_name = input("➕ Enter the song name to add:\n")

            if (song_name.replace(" ", "").isalnum()):

                if (not self.play_list):
                    self.play_list[1] = song_name
                    print("\n✅ Song added successfully!\n")
                    return

                elif (song_name in self.play_list.values()):
                    print("\n❌ Song already exists.\n")

                else:
                    current_number = max(map(int, self.play_list.keys()))
                    self.play_list[str(current_number + 1)] = song_name
                    save_music(self.play_list, self.current_song)

                    print("\n✅ Song added successfully!\n")

                    if not self.battery_manager.consume_battery(2):
                        return

            else:
                print("\n❌ Song name should contain only letters or alphanumeric characters.\n")

    # Method to reorganize the playlist
    def reorganize_playlist(self):
        new_play_list = {}

        if (not self.play_list):
            return False
        else:
            for number, value in enumerate(self.play_list.values(), start=1):
                new_play_list[number] = value

            self.play_list = new_play_list
            return

    # Method to delete a song from the playlist
    def delete_song(self):
        if (not self.play_list):
            print("\n📭 Playlist is empty. Nothing to delete.\n")

        else:
            print("\n" + "═"*16 + " 🎼 PLAYLIST " + "═"*16 + "\n")

            for key, value in self.play_list.items():
                print(f"🎵 {key}. {value}")

            while True:
                choice = input("\n🗑️ Enter the song number to delete: ")

                if (choice.isdigit()):
                    if (choice in self.play_list):

                        if (self.play_list[choice] == self.current_song):
                            stop_music = input("⚠️ Delete the currently playing song? (y/n): ").lower()

                            if (stop_music == "y"):
                                del self.play_list[choice]
                                self.current_song = None

                                self.reorganize_playlist()
                                save_music(self.play_list, self.current_song)

                                print("\n⏹️ Music stopped.")
                                print("✅ Song deleted successfully.\n")

                                if not self.battery_manager.consume_battery(2):
                                    return

                            elif (stop_music == "n"):
                                break

                            else:
                                print("\n❌ Invalid choice.\n")

                        else:
                            del self.play_list[choice]

                            self.reorganize_playlist()
                            save_music(self.play_list, self.current_song)

                            print("\n✅ Song deleted successfully.\n")
                            return

                    else:
                        print("\n❌ Song number not found.\n")

                else:
                    print("\n❌ Choice should be a number.\n")

    # Method to stop the song
    def stop_song(self):
        if self.current_song is None:
            print("\n🎵 No music is currently playing.\n")
            return

        else:
            self.current_song = None
            save_music(self.play_list, self.current_song)
            print("\n⏹️ Music stopped successfully.\n")

    # Method to play music and reduce battery percentage
    def music_manager(self):
        if not self.battery_manager.check_battery():
            return

        self.see_music_menu()

        while True:
            print("\n" + "─"*42)
            print("🎵 What would you like to do?")
            print("─"*42)

            choice = input("\n➡️  Enter your choice: ")
            print()

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
                    self.see_music_menu()
                elif choice == 7:
                    return
                else:
                    print("\n❌ Please enter a valid menu choice.\n")
            else:
                print("\n❌ Error: Choice must be a digit.\n")
