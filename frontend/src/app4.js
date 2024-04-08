
import React, { useState, useEffect } from 'react';
import './App.css';
import Item from './Item'; // Import the Item component

function App() {
  const [items, setItems] = useState([]);
  const [formData, setFormData] = useState({ name: '', description: '', imageUrl: '' });

  useEffect(() => {
    fetch('http://localhost:8000/items')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:8000/items', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => {
        setItems([...items, data]);
        setFormData({ name: '', description: '', imageUrl: '' }); // Clear form
      })
      .catch(error => console.error('Error:', error));
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>https://placebear.com/200/200</p>
        <img src="https://placebear.com/200/200" alt="bear" />
        <p>https://placebacon.com/200/200</p>
        <img src="https://placebacon.com/200/200" alt="bacon" />
        <p>https://placedog.net/200/200</p>
        <img src="https://placedog.net/200/200" alt="doggy" />
        <p>https://placedog.net/200/300</p>
        <img src="https://placedog.net/200/300" alt="doge" />
        <p>https://placekitten.com/200/200</p>
        <img src="https://placekitten.com/200/200" alt="kitty" />
        
      <form onSubmit={handleSubmit}>
          <input type="text" name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
          <input type="text" name="description" placeholder="Description" value={formData.description} onChange={handleChange} required />
          <input type="text" name="imageUrl" placeholder="Image URL" value={formData.imageUrl} onChange={handleChange} required />
          <button type="submit">Add Item</button>
        </form>
        <h1>Items</h1>
        {items.map((item) => (
          <Item key={item.name} item={item} /> // Use the Item component
        ))}
        
      </header>
    </div>
  );
}

export default App;

