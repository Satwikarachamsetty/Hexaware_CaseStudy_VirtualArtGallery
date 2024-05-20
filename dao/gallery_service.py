from abc import ABC, abstractmethod
from util.DBconn import DBConnection

#@-Decorates
class IGalleryService(ABC):
    @abstractmethod
    def addGallery(self, gallery):
        pass

    @abstractmethod
    def updateGallery(self, gallery):
        pass

    @abstractmethod
    def removeGallery(self, gallery_id):
        pass

    @abstractmethod
    def getGalleryById(self, gallery_id):
        pass
    
    @abstractmethod
    def readGallery(self):
        pass

#Multiple Inheritance
class GalleryService(IGalleryService, DBConnection):
    def readGallery(self):
        try:
            self.cursor.execute("Select * from Gallery")
            gallerys = self.cursor.fetchall()  # Get all data
            for gallery in gallerys:
                print(gallery)
            return gallerys
        except Exception as e:
            print(e)
            return None

    def addGallery(self,gallery):
        try:
            self.cursor.execute(
                "INSERT INTO Gallery (GalleryID, Name, Description, Location, Curator, OpeningHours) VALUES (?,?,?,?,?,?)",
                (gallery.GalleryID, gallery.Name, gallery.Description, gallery.Location,gallery.Curator, gallery.OpeningHours),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
            return gallery.GalleryID
        
        except Exception as e:
            print(e)

    def updateGallery(self, gallery):
        self.cursor.execute(
            """
            Update Gallery
            Set Name = ?, Description = ?, Location = ?, Curator = ?, OpeningHours = ?
            where GalleryId = ?
            """,
            ( gallery.Name, gallery.Description, gallery.Location,gallery.Curator, gallery.OpeningHours,gallery.GalleryID),
        )
        self.conn.commit()  # Permanent storing | If no commit then no data
        return True
   
    def removeGallery(self, gallery_id):
        self.cursor.execute("Delete from Gallery Where GalleryID = ?", gallery_id)
        self.conn.commit()

    def getGalleryById(self, gallery_id):
        try:
            print("M")
            self.cursor.execute(
                "Select * from Gallery Where GalleryID = ?", gallery_id
            )
            gallery=self.cursor.fetchone()
            print(gallery)
        except Exception as e:
            print("OOPs",e)





   