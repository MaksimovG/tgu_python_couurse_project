import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import ImageUploadForm from './components/ImageUploadForm';
import ImageCard from './components/ImageCard';
import axios from 'axios';

const App: React.FC = () => {
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [images, setImages] = useState<string[]>([]);

  const toggleFormVisibility = () => {
    setIsFormVisible(!isFormVisible);
  };

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/").then((res) => {console.log(res); setImages(res.data.images)});
  }, []);

  return (
    <div className="App">
      <Header />
      <main className="p-4">
        <button
          onClick={toggleFormVisibility}
          className="bg-green-500 text-white py-2 px-4 rounded-md"
        >
          Upload Image
        </button>

        {isFormVisible && <ImageUploadForm />}

        <div className="grid grid-cols-4 gap-4 mt-4">
          {images.map((imageUrl, index) => (
            <ImageCard key={index} imageUrl={`http://127.0.0.1:8000/${imageUrl}`} />
          ))}
        </div>
      </main>
    </div>
  );
};

export default App;