import React from 'react';

interface ImageCardProps {
  imageUrl: string;
}

const ImageCard: React.FC<ImageCardProps> = ({ imageUrl }) => {
  return (
    <div className="w-1/4 p-2">
      <img src={imageUrl} alt={imageUrl} className="rounded-md shadow-lg" />
    </div>
  );
};

export default ImageCard;