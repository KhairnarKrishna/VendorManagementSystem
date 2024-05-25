import React from 'react';
import './Rating.css';

const Rating = ({ quality_rating_avg }) => {
  const totalStars = 5;
  const stars = [];

  for (let i = 0; i < totalStars; i++) {
    stars.push(
      <span key={i} className={`fa fa-star ${i < quality_rating_avg ? 'checked' : ''}`}></span>
    );
  }

  return <div>{stars}</div>;
};

export default Rating;

