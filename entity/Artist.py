class Artist:
    def __init__(self, ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation):
        self.ArtistID = ArtistID
        self.Name = Name
        self.Biography = Biography
        self.BirthDate = BirthDate
        self.Nationality = Nationality
        self.Website = Website
        self.ContactInformation = ContactInformation

    def getArtistID(self):
        return self.ArtistID

    def setArtistID(self, ArtistID):
        self.ArtistID = ArtistID

    def getName(self):
        return self.Name
    
    def setName(self, Name):
        self.Name = Name

    def getBiography(self):
        return self.Biography

    def setBiography(self, Biography):
        self.Biography = Biography

    def getBirthDate(self):
        return self.BirthDate

    def setBirthDate(self, BirthDate):
        self.BirthDate = BirthDate

    def getNationality(self):
        return self.Nationality

    def setNationality(self, Nationality):
        self.Nationality = Nationality

    def getWebsite(self):
        return self.Website

    def setWebsite(self, Website):
        self.Website = Website

    def getContactInformation(self):
        return self.ContactInformation

    def setContactInformation(self, ContactInformation):
        self.ContactInformation = ContactInformation
