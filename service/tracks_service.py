from Flask_project.rest.top_tracks import track_list

from models.Tracks import Tracks

from Flask_project import db


def tracks_to_db():
    """  Creating an instance of Tracks class and saving it to db"""

    for v in track_list:
        artist_name = v['artist_name']
        album_name = v['album_name']
        track_name = v['track_name']
        track_img_url = v['track_img_url']
        release_date = v['release_date']
        track_url = v['track_url']
        db.session.add(Tracks(artist_name=artist_name, album_name=album_name, track_name=track_name,
                              track_img_url=track_img_url, release_date=release_date,
                              track_url=track_url))


# tracks = tracks_to_db()
# db.session.all(tracks)
db.session.commit()
