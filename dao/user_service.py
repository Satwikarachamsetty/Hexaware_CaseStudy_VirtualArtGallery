from util.DBconn import DBConnection
from myexception.UserNotFoundException import UserNotFoundException
from abc import ABC, abstractmethod

#@-Decorates
class IUserService(ABC):
   
    @abstractmethod
    def addUser(self, user):
        pass

    @abstractmethod
    def updateUser(self, user_id):
        pass

    @abstractmethod
    def removeUser(self, user_id):
        pass

    @abstractmethod
    def getUserById(self, user_id):
        pass

    @abstractmethod
    def readUser(self):
        pass
    
class UserService(IUserService,DBConnection):

    def readUser(self):
        try:
            self.cursor.execute("Select * from [User]")
            users = self.cursor.fetchall()  # Get all data
            for user in users:
                print(user)
        except Exception as e:
            print(e)


    def addUser(self,user):
        try:
            self.cursor.execute(
                "INSERT INTO [User] (UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture) VALUES (?, ?, ?,?,?,?,?,?)",
                (user.UserID, user.Username, user.Password, user.Email, user.FirstName, user.LastName, user.DateOfBirth, user.ProfilePicture),
            )
            #self.conn.commit()  # Permanent storing | If no commit then no data
            return True
        except Exception as e:
            print(e)
    
    def updateUser(self, user_id):
        self.cursor.execute(
            """
            Update [User]
            Set  Username = ?, [Password] =?, Email = ?, FirstName = ?, LastName =?, DateOfBirth = ?, ProfilePicture =?
            where UserID = ?
            """,
            (user_id.UserID, user_id.Username, user_id.Password, user_id.Email, user_id.FirstName, user_id.LastName, user_id.DateOfBirth, user_id.ProfilePicture),
        )
        self.conn.commit()  # Permanent storing | If no commit then no data
   
    def removeUser(self, user_id):
        self.cursor.execute("Delete from [User] Where UserID = ?", user_id)
        self.conn.commit()

    def getUserById(self, user_id):
        try:
            self.cursor.execute(
                "Select * from [User] Where UserID = ?", user_id
            )
            users = self.cursor.fetchall()  # Get all data
            if len(users) == 0:
                raise UserNotFoundException(user_id)
            else:
                print(users)
        except Exception as e:
            print("Ooops Error happened: ", e)