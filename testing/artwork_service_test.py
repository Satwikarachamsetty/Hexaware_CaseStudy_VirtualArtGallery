import unittest
from dao.artwork_service import ArtworkService
from entity.Artwork import Artwork


class TestArtworkServiceModule(unittest.TestCase):
    def setUp(self):
        self.artwork_service = ArtworkService()
    
    def test_add_artwork(self):
        ArtworkID=7
        Title='Earth'
        Description='The Mother'
        CreationDate='2024-05-08'
        Medium='Oil paint'
        ImageURL='https://example.com/earth.jpg'
        artwork = Artwork(ArtworkID, Title, Description, CreationDate, Medium, ImageURL)
        created_artwork_id = self.artwork_service.addArtwork(artwork)
        self.assertIsNotNone(created_artwork_id)

    def test_delete_artwork(self):
        self.test_artwork_id=7
        self.artwork_service.removeArtwork(self.test_artwork_id)
        self.artwork_service.cursor.execute(
            "SELECT * FROM Artwork WHERE ArtworkID= ?", (self.test_artwork_id,)
        )
        artwork = self.artwork_service.cursor.fetchone()
        self.assertIsNone(artwork)    

    def test_update_artwork(self):
        u_ArtworkID = 4
        u_Title = 'Mars'
        u_Description='Another Planet'
        u_CreationDate='2024-05-06'
        u_Medium='Sketch pen' 
        u_ImageURL='https://example.com/mars.jpg'
        update=Artwork(u_ArtworkID, u_Title,u_Description, u_CreationDate, u_Medium, u_ImageURL)
        updated_artwork = self.artwork_service.updateArtwork(update)
        self.assertTrue(updated_artwork)
        

        # Check after updating the movie
        self.artwork_service.cursor.execute(
            "SELECT * FROM Artwork WHERE ArtworkID = ?", (u_ArtworkID,)
        )
        updated_artwork = self.artwork_service.cursor.fetchone()

        self.assertEqual(updated_artwork[0], u_ArtworkID)
        self.assertEqual(updated_artwork[1], u_Title)
        self.assertEqual(updated_artwork[2], u_Description)
        self.assertEqual(updated_artwork[3], u_CreationDate)
        self.assertEqual(updated_artwork[4], u_Medium)
        self.assertEqual(updated_artwork[5], u_ImageURL)

    
    def test_read_artwork(self):
        artworks = self.artwork_service.readArtwork()
        self.assertIsNotNone(artworks)
        self.assertGreater(len(artworks), 0)

if __name__ == "__main__":
    unittest.main()
