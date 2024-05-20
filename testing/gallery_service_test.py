import unittest
from dao.gallery_service import GalleryService
from entity.Gallery import Gallery


class TestGalleryServiceModule(unittest.TestCase):
    def setUp(self):
        self.gallery_service = GalleryService()

    def test_add_gallery(self):
        GalleryID = 9
        Name = "Saketh Museum"
        Description = 'The Organized art museum' 
        Location = 'Chennai'
        Curator = 1
        OpeningHours = '9:00 AM - 6:30 PM'
        gallery = Gallery(GalleryID, Name, Description, Location, Curator, OpeningHours)
        created_gallery_id = self.gallery_service.addGallery(gallery)
        self.assertIsNotNone(created_gallery_id)


    # def test_get_gallery_by_id(self):
    #     gallery = self.gallery_service.getGalleryById(self.test_gallery_id)
    #     self.assertIsNotNone(gallery)
    #     self.assertEqual(gallery[2], "Initial Gallery")
    

    def test_update_gallery(self):
        u_GalleryID = 4
        u_Name = "Arya Museum"
        u_Description = 'The famous art museum' 
        u_Location = 'Delhi'
        u_Curator = 1
        u_OpeningHours = '9:30 AM - 6:30 PM'
        update=Gallery(u_GalleryID,u_Name,u_Description,u_Location,u_Curator,u_OpeningHours)
        updated_gallery = self.gallery_service.updateGallery(update)
        self.assertTrue(updated_gallery)

        # Check after updating the movie
        self.gallery_service.cursor.execute(
            "SELECT * FROM Gallery WHERE GalleryID = ?", (u_GalleryID,)
        )
        updated_gallery = self.gallery_service.cursor.fetchone()

        self.assertEqual(updated_gallery[0], u_GalleryID)
        self.assertEqual(updated_gallery[1], u_Name)
        self.assertEqual(updated_gallery[2], u_Description)
        self.assertEqual(updated_gallery[3], u_Location)
        self.assertEqual(updated_gallery[4], u_Curator)
        self.assertEqual(updated_gallery[5], u_OpeningHours)

    def test_delete_gallery(self):
        self.test_gallery_id = 9
        self.gallery_service.removeGallery(self.test_gallery_id)
        self.gallery_service.cursor.execute(
            "SELECT * FROM Gallery WHERE GalleryID = ?", (self.test_gallery_id,)
        )
        gallery = self.gallery_service.cursor.fetchone()
        self.assertIsNone(gallery)
 
    
    def test_read_gallery(self):
        gallerys = self.gallery_service.readGallery()
        self.assertIsNotNone(gallerys)
        self.assertGreater(len(gallerys), 0)

if __name__ == "__main__":
    unittest.main()
