
from abc import ABC, abstractmethod
from myexception.ArtWorkNotFoundException import ArtWorkNotFoundException
from util.DBconn import DBConnection

class IArtworkService(ABC):
    @abstractmethod
    def addArtwork(self, artwork):
        pass

    @abstractmethod
    def updateArtwork(self, artwork):
        pass

    @abstractmethod
    def removeArtwork(self, artwork_id):
        pass

    @abstractmethod
    def getArtworkById(self, artwork_id):
        pass
    
    @abstractmethod
    def readArtwork(self):
        pass

#Multiple Inheritance
class ArtworkService(IArtworkService, DBConnection):
    def readArtwork(self):
        try:
            self.cursor.execute("Select * from Artwork")
            artworks = self.cursor.fetchall()  # Get all data
            for artwork in artworks:
                print(artwork)
            return artworks
        except Exception as e:
            print(e)
            return None

    def addArtwork(self,artwork):
        try:
            self.cursor.execute(
                "INSERT INTO Artwork (ArtworkID, Title, [Description], CreationDate, [Medium], ImageURL) VALUES (?,?,?,?,?,?)",
                (artwork.ArtworkID, artwork.Title, artwork.Description, artwork.CreationDate,artwork.Medium, artwork.ImageURL),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
            return artwork.ArtworkID
        
        except Exception as e:
            print(e)


    def updateArtwork(self, artwork):
        self.cursor.execute(
            """
            Update Artwork
            Set Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ?
            where ArtworkId = ?
            """,
            ( artwork.Title, artwork.Description, artwork.CreationDate, artwork.Medium, artwork.ImageURL,artwork.ArtworkID),
        )
        self.conn.commit()  # Permanent storing | If no commit then no data
        return True
   
    def removeArtwork(self, artwork_id):
        self.cursor.execute("Delete from Artwork Where ArtworkID = ?", artwork_id)
        self.conn.commit()
        return artwork_id

    def getArtworkById(self, artwork_id):
        try:
            self.cursor.execute(
                "Select * from Artwork Where ArtworkID = ?", artwork_id
            )
            artworks = self.cursor.fetchall()  # Get all data
            if len(artworks) == 0:
                raise ArtWorkNotFoundException(artwork_id)
            else:
                print(artworks)
            return artwork_id
        except Exception as e:
            print("Ooops Error happened: ", e)
