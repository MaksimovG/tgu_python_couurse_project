# app/main.py

import os
import uuid
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel
from repository.images_repository import global_repository
from app.decorators import log_execution, observe_errors

load_dotenv()
UPLOAD_DIR = os.getenv('UPLOAD_DIR')
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешены запросы с любого источника
    allow_credentials=True,
    allow_methods=["*"], # Разрешены все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"] # Разрешены все заголовки
)

@app.get("/")
@log_execution
@observe_errors
async def read_root():
    return {"images": global_repository.get_images()}


class UploadResponse(BaseModel):
    message: str
    image_path: str
    size: int

@app.post("/upload/")
@log_execution
@observe_errors
async def uppoad_file(file: UploadFile = File(...)):
    """Загружает файл и возвращает информацию о нем."""
    try:
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="Файл должен быть изображением")

        content = await file.read()
        file_extension = Path(file.filename).suffix
        file_name = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        
        with open(file_path, "wb") as f:
            f.write(content)
        
        global_repository.add_image(file_path)
        print(global_repository.get_images())
        
        return UploadResponse(message="Изображение успешно загружено", image_path=file_path, size=len(content))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/{UPLOAD_DIR}/{image_name}")
async def get_image(image_name: str):
    """Метод для получения изображения по имени."""
    file_path = os.path.join(UPLOAD_DIR, image_name)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(file_path)