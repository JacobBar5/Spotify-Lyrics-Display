from pprint import pprint
import requests

import apis.config as config


class SongInfo():

    def getCurrentSong(access_token):
        response = requests.get(
            config.SPOTIFY_CURRENT_TRACK_URL, 
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )
        json_response = response.json()


        track_name = json_response['item']['name']

        artists = [artist for artist in json_response['item']['artists'] ]
        
        artist_names = ', '.join(
            [artist['name'] for artist in artists]
            )

        link = json_response['item']['external_urls']['spotify']

        current_song_info = {
            'name': track_name,
            'artists': artists,
            'link': link
        }

        return current_song_info