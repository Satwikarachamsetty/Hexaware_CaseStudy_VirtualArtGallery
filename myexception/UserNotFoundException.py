class UserNotFoundException(Exception):
     def __init__(self, UserID):
        super().__init__(f"User with {UserID} is not Found")