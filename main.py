#region
#
# Objectives needed to get lyrics:
#  - detect song that playing on spotify ------------> Spotify API used
#  - get artist and song name
#  - crawl website of song and get the lyrics ----------> Genius API used instead
#        NOTE: azlyrics.com
#        <!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->
#     
# Objectives to display lyrics:
#  - create app window WITH updating on song change funtionality
#     - need song change check
#  - try to predict/get next song that will played ahead of time (?)
#
# Errors to be handeled:
#  - no song playing
#  - Spotify is playing advertisement
#  - no internet connection
#  - mutiple remasters of same song (year of release could resolve?)
#  - expiration of Spotify token (?)
#  - no lyrics for song (ex: intrumental versions)
#
#endregion


from apis.getLyrics import Lyrics
from apis.getSongInfo import SongInfo
import apis.config as config

import time
from pprint import pprint

while True:
    current_song_info = SongInfo.getCurrentSong( config.SPOTIFY_TOKEN )
    # pprint(current_song_info, indent = 3)


    song_name = current_song_info['name']
    print("\n ======= \nsong name: "+song_name)

    song_artists_list = current_song_info['artists']
    print("artists: "+song_artists_list)

    song_link = current_song_info['link']
    print("Spotify song link: "+song_link)

    songArtist = [ song_name, song_artists_list ] 
    songLyrics = Lyrics.textLyrics( songArtist )
    print(songLyrics)

    time.sleep(10)