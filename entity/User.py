class User:
    def __init__(self, UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture):
        self.UserID = UserID
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.ProfilePicture = ProfilePicture

    def getUserID(self):
        return self.UserID

    def setUserID(self, UserID):
        self.UserID = UserID

    def getUsername(self):
        return self.Username

    def setUsername(self, Username):
        self.Username = Username

    def getPassword(self):
        return self.Password

    def setPassword(self, Password):
        self.Password = Password

    def getEmail(self):
        return self.Email

    def setEmail(self, Email):
        self.Email = Email

    def getFirstName(self):
        return self.FirstName

    def setFirstName(self, FirstName):
        self.FirstName = FirstName

    def getLastName(self):
        return self.LastName

    def setLastName(self, LastName):
        self.LastName = LastName

    def getDateOfBirth(self):
        return self.DateOfBirth

    def setDateOfBirth(self, DateOfBirth):
        self.DateOfBirth = DateOfBirth

    def getProfilePicture(self):
        return self.ProfilePicture

    def setProfilePicture(self, ProfilePicture):
        self.ProfilePicture = ProfilePicture
