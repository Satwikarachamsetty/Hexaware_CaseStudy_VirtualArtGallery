from util.DBconn import DBConnection
from myexception.UserNotFoundException import UserNotFoundException
from abc import ABC, abstractmethod

#@-Decorates
class IUserFavoriteArtworkService(ABC):
   
    @abstractmethod
    def addUserFavoriteArtwork(self,artwork_id):
        pass

    @abstractmethod
    def removeUserFavoriteArtwork(self, user_id):
        pass

    @abstractmethod
    def getUserFavoriteArtworkById(self, user_id):
        pass

    @abstractmethod
    def readUserFavoriteArtwork(self):
        pass
    
class UserFavoriteArtworkService(IUserFavoriteArtworkService,DBConnection):
    
    def readUserFavoriteArtwork(self):
        try:
            self.cursor.execute("Select * from User_Favorite_Artwork")
            artworks = self.cursor.fetchall()  # Get all data
            for artwork in artworks:
                print(artwork)
        except Exception as e:
            print(e)
    
    def addUserFavoriteArtwork(self,artwork_id):
        try:
            self.cursor.execute(
                "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (?, ?)",
                (artwork_id.UserID, artwork_id.ArtworkID),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
            return True
        except Exception as e:
            print(e)
    

    def removeUserFavoriteArtwork(self, user_id):
        self.cursor.execute("Delete from User_Favorite_Artwork Where UserID = ?", user_id)
        #self.conn.commit()

    
    def getUserFavoriteArtworkById(self, user_id):
        try:
            self.cursor.execute(
                "Select * from User_Favorite_Artwork Where UserID = ?", user_id
            )
            artworks = self.cursor.fetchall()  # Get all data
            if len(artworks) == 0:
                raise UserNotFoundException(user_id)
            else:
                print(artworks)
        except Exception as e:
            print("Ooops Error happened: ", e)