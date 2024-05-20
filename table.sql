Create Database HexawareArtDB
use HexawareArtDB

-- Artwork table
CREATE TABLE Artwork (
    ArtworkID INT PRIMARY KEY,
    Title VARCHAR(255),
    [Description] TEXT,
    CreationDate DATE,
    [Medium] VARCHAR(100),
    ImageURL VARCHAR(255)
);

-- Artist table
CREATE TABLE Artist (
    ArtistID INT PRIMARY KEY,
    [Name] VARCHAR(255),
    Biography TEXT,
    BirthDate DATE,
    Nationality VARCHAR(100),
    Website VARCHAR(255),
    ContactInformation VARCHAR(255)
);

-- User table
CREATE TABLE [User] (
    UserID INT PRIMARY KEY,
    Username VARCHAR(50),
    [Password] VARCHAR(50),
    Email VARCHAR(255),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    ProfilePicture VARCHAR(255)
);

-- Gallery table
CREATE TABLE Gallery (
    GalleryID INT PRIMARY KEY,
    [Name] VARCHAR(255),
    [Description] TEXT,
    [Location] VARCHAR(255),
    Curator INT,  
    OpeningHours VARCHAR(255),
    FOREIGN KEY (Curator) REFERENCES Artist(ArtistID)
);

-- Junction table for User - FavoriteArtwork (Many-to-Many)
CREATE TABLE User_Favorite_Artwork (
    UserID INT,
    ArtworkID INT,
    PRIMARY KEY (UserID, ArtworkID),
    FOREIGN KEY (UserID) REFERENCES [User](UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)
);

-- Junction table for Artwork - Gallery (Many-to-Many)
CREATE TABLE Artwork_Gallery (
    ArtworkID INT,
    GalleryID INT,
    PRIMARY KEY (ArtworkID, GalleryID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
    FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID)
);