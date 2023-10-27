class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        self.add_song_to_count()
        self.add_to_genres(self)
        self.add_to_artists(self)
        self.add_to_genre_count(self)
        self.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if getattr(song, "_genre") not in cls.genres:
            cls.genres.append(getattr(song, "_genre"))

    @classmethod
    def add_to_artists(cls, song):
        if getattr(song, "_artist") not in cls.artists:
            cls.artists.append(getattr(song, "_artist"))

    @classmethod
    def add_to_genre_count(cls, song):
        if cls.genre_count.get(song._genre):
            cls.genre_count[song._genre] += 1
        else:
            cls.genre_count[song._genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, song):
        if cls.artist_count.get(song._artist):
            cls.artist_count[song._artist] += 1
        else:
            cls.artist_count[song._artist] = 1
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, artist):
        self._artist = artist

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre


    
# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
