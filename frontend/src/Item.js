import React from 'react';

function Item({ item }) {
  return (
    <div key={item.name}>
      <h2>{item.name}</h2>
      <p>{item.description}</p>
      <img src={item.imageUrl} alt={item.name} style={{ width: '100px' }} />
    </div>
  );
}

export default Item;
