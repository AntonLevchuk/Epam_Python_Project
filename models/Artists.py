from Flask_project import db


class Artists(db.Model):
    """ Artist's model """

    __tablename__ = 'artists'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    artist_id = db.Column(db.String(128), nullable=False, unique=True)
    artist_name = db.Column(db.String(128), nullable=False, unique=True)
    genres = db.Column(db.String(128), nullable=False)
    artist_url = db.Column(db.String(128), nullable=False)
    artist_img_url = db.Column(db.String(128), nullable=False)
    about_artists = db.Column(db.Text)

    def __init__(self, artist_id, artist_name, genres, artist_url, artist_img_url, about_artists):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.genres = genres
        self.artist_url = artist_url
        self.artist_img_url = artist_img_url
        self.about_artists = about_artists

    def __repr__(self):
        return f"Artist id: {self.artist_id}, artist's name: {self.artist_name}"