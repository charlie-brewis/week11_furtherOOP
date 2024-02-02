TAB = "   "

class Song:

    def __init__(self, name: str, artist: str, song_length: int):
        self.name = name
        self.artist = artist
        # Measured in seconds
        #! No error checking here
        self.length = int(song_length)

    def get_name(self):
        return self.name

    def __str__(self):
        return f"'{self.name}'[{self.length // 60}:{self.length % 60 :02}] by {self.artist}"



class Playlist:

    def __init__(self, playlist_name: str, initial_songs: list[Song]):
        self.name = playlist_name
        self.songs = initial_songs
        self.commands = {
            "help" : self.command_help,
            "add" : self.command_add,
            "remove" : self.command_remove
        }

    def add_song(self, song: Song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            print("Song already in playlist.")
    
    def remove_song(self, song: Song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print("Song not in playlist.")

    def get_name(self):
        return self.name
    
    def display(self):
        print('\n' + TAB + self.name)
        if len(self.songs) == 0:
            print(TAB + TAB +"Playlist is empty! :(")
            return
        for song in self.songs:
            print(TAB + TAB + str(song))

    def enter_command(self):
        while True:
            self.display()
            print('\n' + TAB + "Please enter a command (type help for list of commands):")
            command = input(">> ").split(', ')
            if command[0] in self.commands:
                self.commands[command[0]](command)
            elif command[0] == "back":
                return
            else:
                print("Error: Command not found")

    def command_help(self, command: list[str]):
        print(f"{TAB}Command 1){TAB}add, SONG_NAME, ARTISTS, SONG_LENGTH_IN_SECS")
        print(f"{TAB}Command 2){TAB}remove, SONG_NAME")
        print(f"{TAB}Command 3){TAB}back")

    def command_add(self, command):
        if len(command) == 4:
            if command[-1].isdigit():
                self.add_song(Song(*command[1:]))
            else:
                print("Error: Invalid song length")
        else:
            print("Error: Invalid add command")

    def command_remove(self, command):
        if len(command) == 2:
            song_name = command[1]
            for song in self.songs:
                if song.get_name() == song_name:
                    self.songs.remove(song)
                    return 
            print("Error: Song not found in playlist")
        else:
            print("Error: Invalid remove command")

    def __str__(self):
        return self.name



class Spotify:
    
    def __init__(self):
        self.all_songs = self.INTIALISE_SONGS()
        self.all_playlists = self.INITALISE_PLAYLISTS()
        self.commands = {
            "help" : self.command_help,
            "select" : self.command_select,
            "remove" : self.command_remove,
            "new" : self.command_new
        }

    def INTIALISE_SONGS(self) -> list[Song]:
        songs = []
        songs.append(Song("Cut - 1990 Demo", "The Cure", 213))
        songs.append(Song("Grace", "Jeff Buckley", 322))
        songs.append(Song("It's Oh So Quiet", "Bjork", 218))
        songs.append(Song("Sour Times", "Portishead", 252))
        songs.append(Song("Beetlebum - 2012 Remaster", "Blur", 305))
        songs.append(Song("Infinite", "Eminem", 252))
        songs.append(Song("Doomsday", "MF DOOM", 298))
        songs.append(Song("C.R.E.A.M.", "Wu-tang Clan", 252))
        return songs

    def INITALISE_PLAYLISTS(self) -> list[Playlist]:
        playlists = []
        playlists.append(Playlist("Alternative 90s", self.all_songs[:4]))
        playlists.append(Playlist("Rap", self.all_songs[5:]))
        return playlists
    
    def display_all_playlists(self):
        print('\n' + TAB + "Select a playlist:")
        for playlist in self.all_playlists:
            print(TAB + TAB + str(playlist))

    def enter_command(self):
        while True:
            self.display_all_playlists()
            print('\n' + TAB + "Please enter a command (type help for list of commands):")
            command = input(">> ").split(', ')
            if command[0] in self.commands:
                self.commands[command[0]](command)
            elif command[0] == "quit":
                return
            else:
                print("Error: Command not found")
    
    def command_help(self, command):
        print(f"{TAB}Command 1){TAB}select, PLAYLIST_NAME")
        print(f"{TAB}Command 2){TAB}remove, PLAYLIST_NAME")
        print(f"{TAB}Command 3){TAB}new, PLAYLIST_NAME")
        print(f"{TAB}Command 4){TAB}quit")

    def command_select(self, command):
        if len(command) == 2:
            playlist_name = command[1]
            for playlist in self.all_playlists:
                if playlist.get_name() == playlist_name:
                    playlist.enter_command()
                    return
            print("Error: Playlist not found in app")
        else:
            print("Error: Invalid select command")

    def command_remove(self, command):
        if len(command) == 2:
            playlist_name = command[1]
            for playlist in self.all_playlists:
                if playlist.get_name() == playlist_name:
                    self.all_playlists.remove(playlist)
                    return
            print("Error: Playlist not found in app")
        else:
            print("Error: Invalid remove command")
    
    def command_new(self, command):
        if len(command) == 2:
            playlist_name = command[1]
            new_playlist = Playlist(playlist_name, [])
            self.all_playlists.append(new_playlist)
            new_playlist.enter_command()
        else:
            print("Error: Invalid new command")
            



    def main_loop(self):
        # while True:
        self.enter_command()



def main():
    # while True:
    #     playlist_name = input("Select a playlist:\n")
    app = Spotify()
    # print(TAB + "Select a playlist:")
    # app.display_all_playlists()
    # app.select_playlist()
    # app.selected_playlist.enter_command()
    app.main_loop()

    '''
    1) Select playlist + view
    2) add song or select song
    3) view 
    4) can remove
    '''

main()