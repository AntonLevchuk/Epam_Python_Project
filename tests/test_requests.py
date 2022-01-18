import unittest

import requests

from Flask_project.rest.Refreshing_Access_Token import refreshed_token, refresh_token, base64_client_data


class Spotify_requests_test(unittest.TestCase):
    """ Testing the Spotify requests (refreshing access token, get top artists, get top tracks)"""

    endpoint_artists = 'https://api.spotify.com/v1/me/top/artists'  # for artists
    endpoint_tracks = 'https://api.spotify.com/v1/me/top/tracks'  # for tracks

    get_params = {
        'time_range': 'medium_term',
        'limit': '50',
        'offset': '0'
    }

    get_header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {refreshed_token}'
    }

    def test_1_get_artists(self, endpoint_artists=endpoint_artists):
        """ Test request to 'spotify artists' """

        r = requests.get(endpoint_artists, params=self.get_params, headers=self.get_header)
        self.assertEqual(r.status_code, 200)

    def test_1_get_tracks(self, endpoint_tracks=endpoint_tracks):
        """ Test request to 'spotify tracks' """

        r = requests.get(endpoint_tracks, params=self.get_params, headers=self.get_header)
        self.assertEqual(r.status_code, 200)

    ################ Testing refreshing of the access token ###################################

    endpoint_token = 'https://accounts.spotify.com/api/token'

    params = {
        'scope': 'user-top-read'
    }

    def test_1_refresh_access_token(self, endpoint_token=endpoint_token, params=params):
        """ Test request to refresh access token """

        if params is None:
            params = params
        r = requests.post(endpoint_token, data={'grant_type': 'refresh_token', 'refresh_token': refresh_token},
                          params=params, headers={'Authorization': 'Basic ' + base64_client_data})
        self.assertEqual(r.status_code, 200)
