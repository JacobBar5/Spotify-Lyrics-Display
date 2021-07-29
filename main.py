#region
#
# Objectives needed to get lyrics:
#  - detect song that playing on spotify ----------> Spotify API used
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
#endregion

from apis.getLyrics import Lyrics

songArtist = ["are you bored yet", "walLoWs"] 

songLyrics = Lyrics.textLyrics( songArtist )

print(songLyrics)