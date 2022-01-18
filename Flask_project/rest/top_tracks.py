from Flask_project.rest.Refreshing_Access_Token import refreshed_token
from Flask_project import db

import requests

import json


class Get_Top_Tracks:
    """ The class which sending requests to Spotify API to take top tracks """

    def __init__(self):
        self.refreshed_token = refreshed_token
        self.type_item = 'tracks'
        self.endpoint = f'https://api.spotify.com/v1/me/top/{self.type_item}'

        self.get_params = {
            'time_range': 'medium_term',
            'limit': '50',
            'offset': '0'
        }

        self.get_header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {refreshed_token}'
        }

    def get_items(self):
        query = self.endpoint

        response = requests.get(query, params=self.get_params, headers=self.get_header)

        response_tracks = response.json()
        return response_tracks


obj_tracks = Get_Top_Tracks()
res_tracks = obj_tracks.get_items()

res_items = json.dumps(res_tracks)

res_items_loads = json.loads(res_items)

items = res_items_loads['items']


def show_tracks():
    """ Sorting data from API """

    tracks_list = []
    for obj in res_items_loads['items']:
        tracks_list.append({'artist_name': obj['album']['artists'][0]['name'],
                            'album_name': obj['album']['name'],
                            'track_name': obj['name'],
                            'track_img_url': obj['album']['images'][0]['url'],
                            'release_date': obj['album']['release_date'],
                            'track_url': obj['external_urls']['spotify']})

    return tracks_list


track_list = show_tracks()
