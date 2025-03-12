import React, { useState } from 'react';
import axios from 'axios';

const ImageUploadForm: React.FC = () => {
  const [image, setImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null); // Для предпросмотра изображения
  const [brightness, setBrightness] = useState(1);
  const [contrast, setContrast] = useState(1);

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      const file = e.target.files[0];
      setImage(file);

      // Создание URL для предпросмотра изображения
      const objectUrl = URL.createObjectURL(file);
      setImagePreview(objectUrl);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!image) {
      return;
    }

    const formData = new FormData();
    formData.append('image', image);
    formData.append('brightness', brightness.toString());
    formData.append('contrast', contrast.toString());

    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Вывести результат
      alert('Image processed: ' + response.data.imageUrl);
    } catch (error) {
      console.error(error);
      alert('Error uploading image');
    }
  };

  return (
    <div className="p-4 bg-gray-100 rounded-md shadow-md w-96 mx-auto">
      <h2 className="text-xl mb-4">Upload and Apply Filters</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleImageChange} className="mb-4" />
        
        {/* Отображение изображения после выбора */}
        {imagePreview && (
          <div className="mb-4">
            <h3 className="text-lg">Image Preview:</h3>
            <img
              src={imagePreview}
              alt="Preview"
              className="w-full h-auto border border-gray-300 rounded-md"
            />
          </div>
        )}

        <div className="mb-4">
          <label className="block mb-2">Brightness</label>
          <input
            type="range"
            min="0"
            max="2"
            step="0.1"
            value={brightness}
            onChange={(e) => setBrightness(parseFloat(e.target.value))}
            className="w-full"
          />
        </div>
        <div className="mb-4">
          <label className="block mb-2">Contrast</label>
          <input
            type="range"
            min="0"
            max="2"
            step="0.1"
            value={contrast}
            onChange={(e) => setContrast(parseFloat(e.target.value))}
            className="w-full"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded-md"
        >
          Upload and Apply Filter
        </button>
      </form>
    </div>
  );
};

export default ImageUploadForm;
