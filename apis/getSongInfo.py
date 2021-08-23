import requests

import apis.config as config


class SongInfo():

    access_token = config.SPOTIFY_TOKEN

    def getCurrentSong(access_token):
        response = requests.get(
            config.SPOTIFY_CURRENT_TRACK_URL, 
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )
        json_response = response.json()


        track_name = json_response['item']['name']
        link = json_response['item']['external_urls']['spotify']
        artists = [ artist for artist in json_response['item']['artists'] ]
        all_artist_names = ', '.join(  [artist['name'] for artist in artists]  )

        current_song_info = {
            'name': track_name,
            'artists': all_artist_names,
            'link': link
        }

        return current_song_info