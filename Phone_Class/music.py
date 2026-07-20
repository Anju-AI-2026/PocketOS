class MusicManager:

    def __init__(self):
        self.play_list = {}
        self.current_song = None

    # Method to see the music menu
    def see_menu(self):
        print("="*35)
        print("            MUSIC MENU")
        print("="*35)
        print("1.Play music")
        print("2.Show play list")
        print("3.Add song")
        print("4.Delete song")
        print("5.Stop music")
        print("6.See menu")
        print("7.Back")  

    #Method to show the playlist
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
