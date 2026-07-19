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
