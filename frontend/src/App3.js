


import React, { useState, useEffect } from 'react';
import './App.css';

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
        <h1>Items</h1>
        {items.map(item => (
          <div key={item.name}>
            <h2>{item.name}</h2>
            <p>{item.description}</p>
            <img src={item.imageUrl} alt={item.name} style={{ width: '100px' }} />
          </div>
        ))}
        <form onSubmit={handleSubmit}>
          <input type="text" name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
          <input type="text" name="description" placeholder="Description" value={formData.description} onChange={handleChange} required />
          <input type="text" name="imageUrl" placeholder="Image URL" value={formData.imageUrl} onChange={handleChange} required />
          <button type="submit">Add Item</button>
        </form>
      </header>
    </div>
  );
}

export default App;

