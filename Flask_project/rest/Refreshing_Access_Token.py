import requests
import base64

# Get New Release - no scope
# Get Top Item - scope: user-top-read
# Get Available Genre Seeds - no scope
# Get Several Browse Categories - no scope


client_id = '7dd00a3467cf493dbbc5d95cb838c5d7'
client_secret = '4ebb599bbdc944fd81ed84c71db4d53c'
redirect_url_encoded = 'https%3A%2F%2Fgithub.com%2FAntonLevchuk'
refresh_token = "AQBp6O5vU2G49aVMZoN1KZGiLIiiOYWa1U0qgMDHPBBdtDPaqb7gnzeTwV1nvZTu3oBM_3xiwvt8pbJ-8QtHyToH-eRAabrb2fbJcd_wLuItSm7ikigGDCy__YJSYTZfO1Y",

# query = 'https://accounts.spotify.com/authorize?client_id=7dd00a3467cf493dbbc5d95cb838c5d7&response_type=code&redirect_uri=https%3A%2F%2Fgithub.com%2FAntonLevchuk&scope=user-top-read'

client_data = f'{client_id}:{client_secret}'
client_data_bytes = client_data.encode('ascii')
base64_bytes_client_data = base64.b64encode(client_data_bytes)
base64_client_data = base64_bytes_client_data.decode('ascii')


class RefreshToken:
    """ The class which is automatically refreshing the access token for Spotify API """

    def __init__(self):
        self.refresh_token = refresh_token
        self.client_data = base64_client_data

    def refresh(self):

        query = 'https://accounts.spotify.com/api/token'

        get_params = {
            'scope': 'user-top-read'
        }

        response = requests.post(query, data={'grant_type': 'refresh_token', 'refresh_token': refresh_token},
                                 params=get_params, headers={'Authorization': 'Basic ' + self.client_data})

        response_object = response.json()
        # print(response_object)
        return response_object['access_token']


obj = RefreshToken()
refreshed_token = obj.refresh()

code = 'AQBQBPx5RHV6WxxPBFhiAm7eP8_pc7ADLbWeunb0slLZnQoHsLUTtq4iw5d7vlRnL8PipnAeAeBtV4jSqBf4Vno3U27srUiNjqmlv5hfbOXpU1y5kagAfazTI8hZ0UhKitNQAV4tvNlE3DyTI_Ltag9KRn4yt9o19t1OI6yVfNHdPYBGZuyhLsQdvNOiq2Lrt8A'


class GetToken:
    """ The class which sent request to get the access token for Spotify API  """

    def __init__(self):
        self.code = code
        self.client_data = base64_client_data
        self.redirect_uri = redirect_url_encoded

    def get_access_token(self):

        query = 'https://accounts.spotify.com/api/token'

        response = requests.post(query, params={'grant_type': 'authorization_code', 'code:': f'{self.code}',
                                                'redirect_uri:': f'{redirect_url_encoded}'},
                                 headers={'Authorization': 'Basic ' + self.client_data})

        return response
