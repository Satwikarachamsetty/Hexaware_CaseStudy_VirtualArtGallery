class Gallery:
    def __init__(self, GalleryID, Name, Description, Location, Curator, OpeningHours):
        self.GalleryID = GalleryID
        self.Name = Name
        self.Description = Description
        self.Location = Location
        self.Curator = Curator
        self.OpeningHours = OpeningHours

    def getGalleryID(self):
        return self.GalleryID

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getLocation(self):
        return self.Location

    def getCurator(self):
        return self.Curator

    def getOpeningHours(self):
        return self.OpeningHours
    
    
    def setGalleryID(self,GalleryID):
        self.GalleryID = GalleryID

    def setName(self,Name):
        self.Name = Name

    def setDescription(self,Description):
        self.Description = Description

    def setLocation(self,Location):
        self.Location = Location

    def setCurator(self,Curator):
        self.Curator = Curator

    def setOpeningHours(self,OpeningHours):
        self.OpeningHours =OpeningHours
    