import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/items')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {items.map(item => (
          <div key={item.name}>
            <h2>{item.name}</h2>
            <p>{item.description}</p>
            <img src={item.imageUrl} alt={item.name} style={{ width: '100px' }} />
          </div>
        ))}
      </header>
    </div>
  );
}

export default App;