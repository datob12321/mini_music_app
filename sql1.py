import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, URL
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine("mysql+mysqlconnector://root:dato.123.mysql@localhost/mymusic", echo=True)
Base = declarative_base()


class Artists(Base):
    __tablename__ = 'artists'
    artist_id = Column('artistID', Integer, autoincrement=True, primary_key=True)
    first_name = Column('firstname', String(50), nullable=False)
    last_name = Column('lastname', String(50))
    birth_date = Column('birth_date', Date)
    country = Column('country', String(50), nullable=False)
    monthly_listeners = Column('monthly_listeners', Integer)

    def __init__(self, first_name, last_name, birth_date, country, monthly_listeners):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.country = country
        self.monthly_listeners = monthly_listeners

    def __repr__(self):
        if self.last_name == None:
            return f'{self.artist_id}: {self.first_name}'
        else:
            return f'{self.artist_id}: {self.first_name} {self.last_name}'

    @classmethod
    def get_all(cls):
        all_artists = session.query(Artists).all()
        return all_artists

    @classmethod
    def get_songs(cls, artist_name):
        artist = session.query(Artists).filter_by(first_name=artist_name).first()
        all_songs = session.query(Songs).filter(Songs.artist_id==artist.artist_id).all()
        return all_songs

    def get_info(self):
        return session.query(ArtistInfo).filter(ArtistInfo.artist_id == self.artist_id).first()



class Songs(Base):
    __tablename__ = 'songs'
    song_id = Column('songID', Integer, autoincrement=True, primary_key=True)
    song_name = Column('song_name', String(50), nullable=False)
    song_language = Column('song_language', String(50), nullable=False)
    song_genre = Column('song_genre', String(50), nullable=False)
    release_year = Column('release_year', Integer)
    youtube_likes = Column('youtube_likes', Integer)
    artist_id = Column('artistID', Integer, ForeignKey('artists.artistID'))

    def __init__(self, song_name, song_language, song_genre, release_year, youtube_likes, artist_id):
        self.song_name = song_name
        self.song_language = song_language
        self.song_genre = song_genre
        self.release_year = release_year
        self.youtube_likes = youtube_likes
        self.artist_id = artist_id

    def __repr__(self):
        return f'{self.song_id}: {self.song_name}'

    @classmethod
    def get_all(cls):
        all_songs = session.query(Songs).all()
        return all_songs

    def get_lyrics(self):
        song_id = self.song_id
        lyrics = session.query(Lyrics).filter_by(song_id=song_id).first()
        return lyrics

    def get_url(self):
        song_id = self.song_id
        url = session.query(SongUrl).filter_by(song_id=song_id).first()
        return url

    def get_artist(self):
        artist_id = self.artist_id
        artist = session.query(Artists).filter(Artists.artist_id == artist_id).first()
        return artist


class ArtistInfo(Base):
    __tablename__ = 'artists_info'
    info_id = Column('infoID', Integer, autoincrement=True, primary_key=True)
    artist_photo = Column('artist_photo', String(250))
    content = Column('content', String(15000), nullable=False)
    artist_id = Column('artistID', Integer, ForeignKey('artists.artistID'))

    def __init__(self, artist_photo, content, artist_id):
        self.artist_photo = artist_photo
        self.content = content
        self.artist_id = artist_id

    def __repr__(self):
        return f'info id: {self.info_id}'


class Lyrics(Base):
    __tablename__ = 'lyrics'
    lyric_id = Column('lyricID', Integer, autoincrement=True, primary_key=True)
    lyric = Column('lyric', String(15000), nullable=False)
    song_id = Column('songID', Integer, ForeignKey('songs.songID'))

    def __init__(self, lyric, song_id):
        self.lyric, self.song_id = lyric, song_id

    def __repr__(self):
        return f'lyric id: {self.lyric_id}'

    @classmethod
    def get_all(cls):
        return session.query(Lyrics).all()


class SongUrl(Base):
    __tablename__ = 'songs_url'
    urlID = Column('urlID', Integer, autoincrement=True, primary_key=True)
    url = Column('url', String(250), nullable=False)
    song_id = Column('songID', Integer, ForeignKey('songs.songID'))

    def __init__(self, url, song_id):
        self.url = url
        self.song_id = song_id

    def __repr__(self):
        return f'url id: {self.urlID}'

    @staticmethod
    def get_all():
        return session.query(SongUrl).all()



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# artists = session.execute(sqlalchemy.text('''SELECT firstname, lastname, song_name FROM
#                                              artists a JOIN songs
#                                              s ON a.artistID=s.artistID''')).fetchall()

#lyrics = session.execute(sqlalchemy.text("SELECT * FROM lyrics")).fetchall()

paulo = session.query(Artists).filter_by(first_name='Paulo').first()
paulos_id = paulo.artist_id

paulos_songs = session.query(Songs).filter(Songs.artist_id == paulos_id).all()

# print(artists)
# print(lyrics[1][1])
# for song in paulos_songs:
#     print(song.song_name)

#print(paulos_songs[1].get_lyrics().lyric)

artists = Artists.get_all()
#print(artists)
songs = Songs.get_all()

lyrics = Lyrics.get_all()

song_urls = SongUrl.get_all()


#print(songs)
