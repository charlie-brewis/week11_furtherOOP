TAB = "   "

class Song:

    def __init__(self, name: str, artist: str, song_length: int):
        self.name = name
        self.artist = artist
        # Measured in seconds
        self.length = song_length

    def __str__(self):
        return f"'{self.name}'[{self.length // 60}:{self.length % 60}] by {self.artist}"



class Playlist:

    def __init__(self, playlist_name: str, initial_songs: list[Song]):
        self.name = playlist_name
        self.songs = initial_songs
        self.commands = {
            "help" : self.command_help,
            "add" : self.command_add,
            "select" : self.command_select,
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
        print(TAB + self.name)
        for song in self.songs:
            print(TAB + TAB + song)

    def enter_command(self):
        while True:
            print('\n' + TAB + "Please enter a command (type help for list of commands):")
            command = input(">> ").split(' ')
            if command[0] in self.commands:
                self.commands[command[0]](command)
            elif command[0] == "back":
                return
            else:
                print("Error: Command not found")


    def command_help(self, command: list[str]):
        print(f"{TAB}Command 1){TAB}add SONG_NAME ARTISTS SONG_LENGTH_IN_SECS")
        print(f"{TAB}Command 2){TAB}select SONG_NAME")
        print(f"{TAB}Command 3){TAB}back")

    def command_add(self, command):
        pass

    def command_select(self, command):
        pass

    def __str__(self):
        return self.name



class Spotify:
    
    def __init__(self):
        self.all_songs = self.intialise_songs()
        self.all_playlists = self.intialise_playlists()
        self.selected_playlist = None 
        self.selected_song = None

    def intialise_songs(self) -> list[Song]:
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

    def intialise_playlists(self) -> list[Playlist]:
        playlists = []
        playlists.append(Playlist("Alternative 90s", self.all_songs[:4]))
        playlists.append(Playlist("Rap", self.all_songs[5:]))
        return playlists
    
    def display_all_playlists(self):
        for playlist in self.all_playlists:
            print(TAB + TAB + str(playlist))
    
    def select_playlist(self):
        while True:
            selected = input('>> ')
            for playlist in self.all_playlists:
                if playlist.get_name() == selected:
                    self.selected_playlist = playlist
                    return
            print("Error: Playlist not found in app")


def main():
    # while True:
    #     playlist_name = input("Select a playlist:\n")
    app = Spotify()
    print(TAB + "Select a playlist:")
    app.display_all_playlists()
    app.select_playlist()
    app.selected_playlist.enter_command()

    '''
    1) Select playlist + view
    2) add song or select song
    3) view 
    4) can remove
    '''

main()