class ArtWorkNotFoundException(Exception):
     def __init__(self, ArtworkID):
        super().__init__(f"Artwork with {ArtworkID} is not Found")