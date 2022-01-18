from Flask_project.rest.Refreshing_Access_Token import refreshed_token

import requests

import json


class Get_Top_Artists:
    """ The class which sending requests to Spotify API to take top artists """

    def __init__(self):
        self.refreshed_token = refreshed_token
        self.type_item = 'artists'
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

        response_artists = response.json()
        return response_artists


obj_artists = Get_Top_Artists()
res_artists = obj_artists.get_items()

res_items = json.dumps(res_artists)

res_items_loads = json.loads(res_items)

item = res_items_loads['items']


def show_items():
    """ Sorting data from API """

    artists_list = []
    for obj in res_items_loads['items']:
        artists_list.append({'artists_id': obj['id'], 'name': obj['name'], 'genres': obj['genres'],
                             'artists_url': obj['external_urls']['spotify'],
                             'artists_img_url': obj['images'][0]['url'],
                             'about_artists': None})
    return artists_list


top_artists = show_items()

############################# Scraping info about artists ##############################################################

""" 
This func was commented because of it works too long, you can uncomment it when you will make request to
Spotify API and you have some new artists 
"""

# from transliterate import translit
#
# import re
#
# import time
#
# from bs4 import BeautifulSoup
#
# # artists = Artists.query.all()
#
# artists_info = []
#
#
# def get_info():
#     """
#     This func is scrapping 'genius.com' and taking from there the 'about artists',
#     it's searching the artists by their names
#     """
#
#     for item in top_artists:
#         artists_list = [item['name']]
#
#         for name in artists_list:
#             x = 0
#
#             if bool(re.search('[а-яА-Я]', name)) is True:  # Translating the rus alphabet to eng
#                 name = translit(name, language_code='ru', reversed=True)
#             else:
#                 pass
#             name = name.replace('.', '')
#
#             try:
#                 url = f'https://genius.com/artists/{name}'
#                 response = requests.get(url)
#                 response.raise_for_status()
#                 x += 1
#
#                 if x == 20:
#                     time.sleep(1)
#                 soup = BeautifulSoup(response.text, 'lxml')
#                 info = soup.find('p')
#
#                 if info is not None:
#                     item['about_artists'] = info.get_text()
#
#             except HTTPError:
#                 pass
#
#
# get_info()
