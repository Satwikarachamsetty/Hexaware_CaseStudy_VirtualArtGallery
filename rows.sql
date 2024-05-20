-- Artwork
INSERT INTO Artwork (ArtworkID, Title, [Description], CreationDate, [Medium], ImageURL) VALUES
    (1, 'Sun', 'Famous painting', '2024-05-01', 'Oil Pastel', 'https://example.com/sun.jpg'),
    (2, 'Moon', 'Sketching', '2024-05-02', 'Pencil', 'https://example.com/moon.jpg'),
	(3, 'Waterfall', 'Beautiful Waterfall', '2024-05-03', 'Crayon', 'https://example.com/water.jpg'),
    (4, 'Solar System', 'Doodle of Planets', '2024-05-04', 'Sketch Pens', 'https://example.com/solarsystem.jpg')
	;


-- Artist
INSERT INTO Artist (ArtistID, [Name], Biography, BirthDate, Nationality, Website, ContactInformation) VALUES
    (1, 'Shiva', 'Shiva was a Indian painter', '2000-09-01', 'Indian', 'https://www.shiva.net/', 'contact@shiva.com'),
    (2, 'Anika', 'Anika was an Indian Artist', '2000-09-02', 'Indian', 'https://www.anika.net/', 'contact@anika.com'),
	(3, 'Varun', 'Varun was a Indian Artist', '2000-09-03', 'Indian', 'https://www.shiva.net/', 'contact@varun.com'),
    (4, 'Madhu', 'Madhu was an Doodle Artist', '2000-09-04', 'Indian', 'https://www.madhu.net/', 'contact@madhu.com')
	;

-- User
INSERT INTO [User] (UserID, Username, [Password], Email, FirstName, LastName, DateOfBirth, ProfilePicture) VALUES
    (1, 'Rohit1', 'password1', 'rohit@gmail.com', 'Rohit', 'Sharma', '1998-08-01', 'https://example.com/profile/rohit.jpg'),
    (2, 'Anu2', 'password2', 'anu@gmail.com', 'Anu', 'Shetty', '1998-08-02', 'https://example.com/profile/anu.jpg'),
	(3, 'Shivika3', 'password3', 'shivika@gmail.com', 'Shivika', 'Chopra', '1998-08-03', 'https://example.com/profile/shivika.jpg'),
    (4, 'Arjun4', 'password4', 'anu@gmail.com', 'Arjun', 'Anand', '1998-08-04', 'https://example.com/profile/arjun.jpg')
	;

-- Gallery
INSERT INTO Gallery (GalleryID, [Name], [Description], [Location], Curator, OpeningHours) VALUES
    (1, 'Shiva Museum', 'The finest art museums', 'Varanasi', 1, '9:30 AM - 5:30 PM'),
    (2, 'Anika Museum', 'The largest art museum', 'Mumbai', 2, '9:00 AM - 6:00 PM'),
	(3, 'Varun Museum', 'The creative art museums', 'Hyderabad', 3, '10:30 AM - 5:30 PM'),
    (4, 'Madhu Museum', 'The famous art museum', 'Kerala', 4, '10:00 AM - 5:00 PM');

-- User_Favorite_Artwork
INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES
    (1, 1),  -- User 1 likes Artwork 1
    (2, 2),  -- User 2 likes Artwork 2
	(3, 3),  -- User 3 likes Artwork 3
    (4, 4);  -- User 4 likes Artwork 4


-- Artwork_Gallery
INSERT INTO Artwork_Gallery (ArtworkID, GalleryID) VALUES
    (1, 1),  -- Artwork 1 is displayed in Gallery 1
    (2, 2),  -- Artwork 2 is displayed in Gallery 2
	(3, 3),  -- Artwork 3 is displayed in Gallery 3
    (4, 4);  -- Artwork 4 is displayed in Gallery 4

