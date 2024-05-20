from abc import ABC, abstractmethod
from util.DBconn import DBConnection

#@-Decorates
class IArtistService(ABC):
    @abstractmethod
    def addArtist(self, artist):
        pass

    @abstractmethod
    def updateArtist(self, artist):
        pass

    @abstractmethod
    def removeArtist(self, artist_id):
        pass

    @abstractmethod
    def getArtistById(self, artist_id):
        pass

    @abstractmethod
    def readArtist(self):
        pass


#Multiple Inheritance
class ArtistService(IArtistService, DBConnection):

    def readArtist(self):
        try:
            self.cursor.execute("Select * from Artist")
            artists = self.cursor.fetchall()  # Get all data
            for artist in artists:
                print(artist)
        except Exception as e:
            print(e)

    def addArtist(self,artist):
        try:
            self.cursor.execute(
                "INSERT INTO Artist (ArtistID,[Name], Biography, BirthDate, Nationality, Website, ContactInformation) VALUES (?,?,?,?,?,?,?)",
                (artist.ArtistID, artist.Name, artist.Biography, artist.BirthDate,artist.Nationality, artist.Website,artist.ContactInformation),
            )
            #self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)

    def updateArtist(self, artist):
        self.cursor.execute(
            """
            Update Artist
            Set Name = ?, Biography =? , BirthDate =?, Nationality =?, Website =?, ContactInformation=?
            where ArtistId = ?
            """,
            (artist.Name, artist.Biography, artist.BirthDate,artist.Nationality, artist.Website,artist.ContactInformation,artist.ArtistID),
        )
        #self.conn.commit()  # Permanent storing | If no commit then no data
   
    def removeArtist(self, artist_id):
        self.cursor.execute("Delete from Artist Where ArtistID = ?", artist_id)
        #self.conn.commit()

    def getArtistById(self, artist_id):
        try:
            self.cursor.execute(
                "Select * from Artist Where ArtistID = ?", artist_id
            )
            artists = self.cursor.fetchall()  # Get all data
            print(artists)
        except Exception as e:
            print(e)
