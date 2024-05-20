class Artwork:
    def __init__(self, ArtworkID, Title, Description, CreationDate, Medium, ImageURL):
        self.ArtworkID = ArtworkID
        self.Title = Title
        self.Description = Description
        self.CreationDate = CreationDate
        self.Medium = Medium
        self.ImageURL = ImageURL

    def getArtworkID(self):
        return self.ArtworkID

    def setArtworkID(self, ArtworkID):
        self.ArtworkID = ArtworkID

    def getTitle(self):
        return self.Title

    def setTitle(self, Title):
        self.Title = Title

    def getDescription(self):
        return self.Description

    def setDescription(self, Description):
        self.Description = Description

    def getCreationDate(self):
        return self.CreationDate

    def setCreationDate(self, CreationDate):
        self.CreationDate = CreationDate

    def getMedium(self):
        return self.Medium

    def setMedium(self, Medium):
        self.Medium = Medium

    def getImageURL(self):
        return self.ImageURL

    def setImageURL(self, ImageURL):
        self.ImageURL = ImageURL





