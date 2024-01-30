


class Song:

    def __init__(self, name: str, artist: str, song_length: int):
        self.name = name
        self.artist = artist
        # Measured in seconds
        self.length = song_length



class Playlist:

    def __init__(self, playlist_name: str, initial_songs: list[Song]):
        self.name = playlist_name
        self.songs = initial_songs

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



def intialise_songs() -> list[Song]:
    songs = []
    songs.append(Song("Cut - 1990 Demo", "The Cure", 213))
    songs.append(Song("Grace", "Jeff Buckley", 322))
    songs.append(Song("It's Oh So Quiet", "Bjork", 218))
    songs.append(Song("Sour Times", "Portishead", 252))
    songs.append(Song("Beetlebum - 2012 Remaster", "Blur", 305))
    return songs

def intialise_playlists(all_songs: list[Song]) -> list[Playlist]:
    playlists = []
    playlists.append(Playlist("Alternative 90s", all_songs[:4]))
    return playlists

def main():
    all_songs = intialise_songs()
    all_playlists = intialise_playlists(all_songs)
    while True:
        pass
