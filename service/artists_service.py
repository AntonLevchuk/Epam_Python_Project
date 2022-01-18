from Flask_project.rest.top_artists import top_artists

from models.Artists import Artists

from Flask_project import db


def artists_to_db():
    """ Creating an instance of Artists model and saving it to db """

    for i in top_artists:
        artist_id = i['artists_id']
        artist_name = i['name']
        genres = i['genres']
        artist_url = i['artists_url']
        artist_img_url = i['artists_img_url']
        about_artists = i['about_artists']
        # artists = [artist_id, artist_name, genres, artist_url, artist_img_url, about_artists]
        db.session.add(Artists(artist_id=artist_id, artist_name=artist_name, genres=genres,
                               artist_url=artist_url, artist_img_url=artist_img_url,
                               about_artists=about_artists))

# artist = artists_to_db()
# db.session.all(artist)
db.session.commit()