from Flask_project import db


class Tracks(db.Model):
    """ Track's model """

    __tablename__ = 'tracks'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    artist_name = db.Column(db.String(64), nullable=False)
    album_name = db.Column(db.String(64), nullable=False)
    track_name = db.Column(db.String(64), nullable=False, unique=True)
    track_img_url = db.Column(db.String(128), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    track_url = db.Column(db.String(128), nullable=False)

    def __init__(self, artist_name, album_name, track_name, track_img_url, release_date, track_url):
        self.artist_name = artist_name
        self.album_name = album_name
        self.track_name = track_name
        self.track_img_url = track_img_url
        self.release_date = release_date
        self.track_url = track_url

    def __repr__(self):
        return f" Track: {self.track_name}, artist's name: {self.artist_name}"