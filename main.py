#region
# Objectives needed to get lyrics:
#  - detect song that playing on spotify
#    To accomplish:
#     - look into a spotify API or similar
#     - get artist and song name
#  - crawl website of song and get the lyrics
#    To accomplish:
#     - need to detect song spotify is playing
#     - place playing song into azlyrics.com search
#        NOTE: azlyrics.com
#        <!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->
#                > look into Genius API
#                   >>> pip install lyricsgenius
#  - display lytrics in app window
#    To accomplish:
#     - need create app window
#     - allow text on window to be able to be updated
#     - (?) try to predict/get next song that will played ahead of time
#endregion

from apis.getLyrics import Lyrics

songArtist = ["are you bored yet", "walLoWs"] 

songLyrics = Lyrics.textLyrics( songArtist )

print(songLyrics)