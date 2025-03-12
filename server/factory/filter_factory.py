# filters.py

from PIL import Image, ImageEnhance
from enum import Enum
from abc import ABC, abstractmethod

class FilterType(str, Enum):
    BRIGHTNESS = "brightness"
    CONTRAST = "contrast"

class BaseFilter(ABC):
    @abstractmethod
    def apply(self, image: Image.Image, factor: float) -> Image.Image:
        pass

class BrightnessFilter(BaseFilter):
    def apply(self, image: Image.Image, factor: float) -> Image.Image:
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(factor)

class ContrastFilter(BaseFilter):
    def apply(self, image: Image.Image, factor: float) -> Image.Image:
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)

class FilterFactory:
    @staticmethod
    def get_filter(filter_type: FilterType) -> BaseFilter:
        if filter_type == FilterType.BRIGHTNESS:
            return BrightnessFilter()
        elif filter_type == FilterType.CONTRAST:
            return ContrastFilter()
        else:
            raise ValueError("Unsupported filter type")