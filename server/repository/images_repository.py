# repository/images_repository.py

from abc import ABC, abstractmethod

class ImagesRepository(ABC):
    @abstractmethod
    def add_image(self, image_path: str):
        pass
    
    @abstractmethod
    def get_images(self):
        pass
    
    @abstractmethod
    def clear(self):
        pass
    
class inMemoryImagesRepository(ImagesRepository):
    def __init__(self):
        self.images = []
        
    def add_image(self, image_path: str):
        self.images.append(image_path)
        
    def get_images(self):
        return self.images
    
    def clear(self):
        self.images = []
    
global_repository = inMemoryImagesRepository()