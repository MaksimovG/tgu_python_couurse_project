# repository/images_repository.py

import json
from abc import ABC, abstractmethod
from typing import List

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
    def __init__(self, file_name: str = "memory.json"):
        self.file_name = file_name
        
    def _load_images(self) -> List[str]:
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                return data.get("images", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_images(self, images: List[str]):
        with open(self.file_name, "w") as file:
            json.dump({"images": images}, file)

    def add_image(self, image_path: str):
        images = self._load_images()
        images.append(image_path)
        self._save_images(images)

    def get_images(self) -> List[str]:
        return self._load_images()
    
    def clear(self):
        self._save_images([])
    
global_repository = inMemoryImagesRepository()