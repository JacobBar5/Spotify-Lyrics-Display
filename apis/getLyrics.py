from lyricsgenius import Genius
import apis.config as config

class Lyrics():
    def textLyrics(songArtistList):
        genius = Genius(config.token)      
            # NOTE: 'token' is saved under a seperate config file, to create own token, visit: https://genius.com/api-clients

        genius.verbose = False
        
        song = genius.search_song( songArtistList[0] , songArtistList[1] )
        
        return song.lyrics


