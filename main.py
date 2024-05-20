from entity import Artwork,User,Gallery,Artist,User_Favorite_Artwork
from dao import UserService
from dao import ArtworkService
from dao import UserFavoriteArtworkService
from dao import GalleryService
from dao import ArtistService


class MainMenu:

    user_service= UserService()
    artwork_service=ArtworkService()
    userFavoriteArtwork_service=UserFavoriteArtworkService()
    gallery_service= GalleryService()
    artist_service=ArtistService()

    def user_menu(self):
        while True:
            print(
                """      
            1. Add an User
            2. Update an User
            3. Remove an User 
            4. Get User by ID
            5. View all users
            6. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                UserID = int(input("Please enter UserID: "))
                Username = input("Please enter Username: ")
                Password = input("Please enter Password: ")
                Email = input("Please enter Email: ")
                FirstName = input("Please enter Firstname: ")
                LastName = input("Please enter Lastname: ")
                DateOfBirth = input("Please enter Date of birth: ")
                ProfilePicture = input("Please enter Profile pic: ")
                new_user = User(UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture)
                self.user_service.addUser(new_user)

            elif choice == 2:
                UserID = int(input("Please enter UserID: "))
                Username = input("Please enter Username: ")
                Password = input("Please enter Password: ")
                Email = input("Please enter Email: ")
                FirstName = input("Please enter Firstname: ")
                LastName = input("Please enter Lastname: ")
                DateOfBirth = input("Please enter Date of birth: ")
                ProfilePicture = input("Please enter Profile pic: ")
                updated_user = User(Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture, UserID)
                self.user_service.updateUser(updated_user)

            elif choice == 3:
                UserID= int(input("Please tell a user id to delete: "))
                self.user_service.removeUser(UserID)

            elif choice== 4:
                UserID = int(input("Please enter user id: "))
                self.user_service.getUserById(UserID)

            elif choice ==5:
                self.user_service.readUser()
    
            elif choice == 6:
                break

    def artwork_menu(self):
        while True:
            print(
                """      
            1. Add an Artwork
            2. Update and Artwork
            3. Delete an Artwork
            4. Get Artwork details by id
            5. View all Artworks
            6. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
            if choice == 1:
                ArtworkID = int(input("Please enter ArtworkID: "))
                Title = input("Please enter Title: ")
                Description = input("Please enter Description: ")
                CreationDate = input("Please enter CreationDate: ")
                Medium = input("Please enter Medium: ")
                ImageURL = input("Please enter ImageURL: ")
                new_artwork = Artwork(ArtworkID, Title, Description, CreationDate, Medium, ImageURL)
                self.artwork_service.addArtwork(new_artwork)

            elif choice == 2:
                ArtworkID = int(input("Please enter ArtworkID: "))
                Title = input("Please enter Title: ")
                Description = input("Please enter Description: ")
                CreationDate = input("Please enter CreationDate: ")
                Medium = input("Please enter Medium: ")
                ImageURL = input("Please enter ImageURL: ")
                update_artwork = Artwork(Title, Description, CreationDate, Medium, ImageURL ,ArtworkID)
                self.artwork_service.updateArtwork(update_artwork)

            elif choice == 3:
                ArtworkID= int(input("Please tell a artwork id to delete: "))
                self.artwork_service.removeArtwork(ArtworkID)

            elif choice== 4:
                ArtworkID = int(input("Please enter artwork id: "))
                self.artwork_service.getArtworkById(ArtworkID)

            elif choice ==5:
                self.artwork_service.readArtwork()

            elif choice == 6:
                break
            
    def gallery_menu(self):
        while True:
            print(
                """      
            1. Add a gallery
            2. Update gallery
            3. Delete an gallery
            4. Get gallery details by id
            5. View all gallery
            6. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
            if choice == 1:
                GalleryID = int(input("Please enter GalleryID: "))
                Name = input("Please enter Name: ")
                Description = input("Please enter Description: ")
                Location = input("Please enter Location: ")
                Curator = int(input("Please enter Curator: "))
                OpeningHours = input("Please enter openinghours: ")
                new_gallery = Gallery(GalleryID, Name, Description, Location, Curator, OpeningHours)
                self.gallery_service.addGallery(new_gallery)

            elif choice == 2:
                GalleryID = int(input("Please enter GalleryID: "))
                Name = input("Please enter Name: ")
                Description = input("Please enter Description: ")
                Location = input("Please enter Location: ")
                Curator = int(input("Please enter Curator: "))
                OpeningHours = input("Please enter openinghours: ")
                update_gallery = Gallery( Name, Description, Location, Curator, OpeningHours, GalleryID)
                self.gallery_service.updateGallery(update_gallery)

            elif choice == 3:
                GalleryID= int(input("Please tell a gallery id to delete: "))
                self.gallery_service.removeGallery(GalleryID)

            elif choice== 4:
                GalleryID = int(input("Please enter gallery id: "))
                self.gallery_service.getGalleryById(GalleryID)

            elif choice ==5:
                self.gallery_service.readGallery()

            elif choice == 6:
                break
            
    def userFavoriteArtwork_menu(self):
        while True:
            print(
                """      
            1. Add an FavoriteArtwork
            2. Delete an FavoriteArtwork
            3. Get Artwork details by id
            4. View all Favorite Artworks
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                UserID=int(input("Enter user id:"))
                ArtworkID = int(input("Please enter ArtworkID: "))
                new_favorite_artwork = User_Favorite_Artwork(UserID,ArtworkID)
                self.userFavoriteArtwork_service.addUserFavoriteArtwork(new_favorite_artwork) 

            elif choice == 2:
                UserID=int(input("Please tell a user id to delete:"))
                self.userFavoriteArtwork_service.removeUserFavoriteArtwork(UserID)

            elif choice== 3:
                ArtworkID = input("Please enter artwork id: ")
                self.userFavoriteArtwork_service.getUserFavoriteArtworkById(ArtworkID)

            elif choice ==4:
                self.userFavoriteArtwork_service.readUserFavoriteArtwork()

            elif choice == 5:
                break

    def artist_menu(self):
        while True:

            print(
                """
           Welcome to Artist Management :
           
            1. Add an Artist
            2. Update and Artist
            3. Delete an Artist
            4. Get Artist details by id
            5. View all Artists
            6. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
            if choice == 1:
                ArtistID = int(input("Please enter ArtistID: "))
                Name = input("Please enter Name: ")
                Biography = input("Please enter Biography: ")
                BirthDate = input("Please enter BirthDate: ")
                Nationality = input("Please enter Nationality: ")
                Website = input("Please enter Webiste: ")
                ContactInformation = input("Please enter Contact information:")
                new_artist = Artist(ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation)
                self.artist_service.addArtist(new_artist)

            elif choice == 2:
                ArtistID = int(input("Please enter ArtistID: "))
                Name = input("Please enter Name: ")
                Biography = input("Please enter Biography: ")
                BirthDate = input("Please enter BirthDate: ")
                Nationality = input("Please enter Nationality: ")
                Website = input("Please enter Webiste: ")
                ContactInformation = input("Please enter Contact information:")
                update_artist = Artist(Name, Biography, BirthDate, Nationality, Website, ContactInformation,ArtistID)
                self.artist_service.updateArtist(update_artist)

            elif choice == 3:
                ArtistID= int(input("Please tell a artist id to delete: "))
                self.artist_service.removeArtist(ArtistID)

            elif choice== 4:
                ArtistID = int(input("Please enter artist id: "))
                self.artist_service.getArtistById(ArtistID)

            elif choice ==5:
                self.artist_service.readArtist()

            elif choice == 6:
                break
            
def main():
    main_menu = MainMenu()

    while True:
        print(
            """      
               1. User Management  
               2. Artwork Management  
               3. Gallery Management    
               4. Artist Management   
               5. User Favorite Artwork Management  
               6. Exit  
                """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            main_menu.user_menu()
        elif choice == 2:
            main_menu.artwork_menu()
        elif choice == 3:
            main_menu.gallery_menu()
        elif choice == 4:
            main_menu.artist_menu()
        elif choice == 5:
            main_menu.userFavoriteArtwork_menu()
        elif choice == 6:
            main_menu.user_service.close() 
            main_menu.artwork_service.close()
            main_menu.artist_service.close()
            main_menu.gallery_service.close()
            main_menu.userFavoriteArtwork_service.close()
            print("Visit Again Soon....Good Day! 😊\n")
            break


# Task 5 - Keep it in loop
if __name__ == "__main__":
    print("✨ 🎊 Welcome to the Virtual Art Gallery App 🎊 ✨")
    main()

    

