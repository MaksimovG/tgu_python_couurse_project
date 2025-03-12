import os
import pytest
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from app.main import app
from repository.images_repository import global_repository

load_dotenv()
client = TestClient(app)
UPLOAD_DIR = os.getenv('UPLOAD_DIR')

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Очистка репозитория перед и после теста"""
    global_repository.clear()
    yield
    global_repository.clear()
    
def test_get_images():
    """Тест корневого эндпоинта"""
    response = client.get("/")
    assert response.status_code == 200
    assert "images" in response.json()
    
def test_add_image():
    """Тест загрузки корректного изображения"""
    file_path = f"{UPLOAD_DIR}/test.jpg"
    image_size = 1024
    
    with open(file_path, "wb") as f:
        f.write(os.urandom(image_size))
        
    with open(file_path, "rb") as f:
        files = {"file": ("test_image.jpg", f, "image/jpeg")}
        response = client.post("/upload/", files=files)
        
    os.remove(file_path)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Изображение успешно загружено"
    assert response.json()["size"] == image_size
