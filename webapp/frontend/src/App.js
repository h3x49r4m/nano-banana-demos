import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState('');
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Fetch the latest generated image on component mount
    fetch('http://localhost:8000/static/latest_generated_image.png')
      .then(response => {
        if (response.ok) {
          return response.blob();
        }
        // If the latest_generated_image.png doesn't exist, fall back to world.png
        return fetch('http://localhost:8000/static/images/world.png').then(res => res.blob());
      })
      .then(blob => {
        setImage(URL.createObjectURL(blob));
      })
      .catch(error => {
        console.error('Error fetching initial image:', error);
        // Fallback to world.png if there's any error fetching latest_generated_image.png
        fetch('http://localhost:8000/static/images/world.png')
          .then(res => res.blob())
          .then(blob => setImage(URL.createObjectURL(blob)));
      });
  }, []);

  const handleSubmit = () => {
    setLoading(true);
    const formData = new FormData();
    formData.append('prompt', prompt);
    // Need to fetch the image blob again to send it to the backend
    fetch(image)
      .then(response => response.blob())
      .then(blob => {
        formData.append('image', blob, 'image.png');
        fetch('http://localhost:8000/generate_image/', {
          method: 'POST',
          body: formData,
        })
        .then(response => response.blob())
        .then(blob => {
          setImage(URL.createObjectURL(blob));
          setLoading(false);
        })
        .catch(error => {
          console.error('Error generating image:', error);
          setLoading(false);
        });
      });
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="App">
      <div className="App-container">
        {loading && (
          <div className="loading-overlay">
            <div className="spinner"></div>
          </div>
        )}
        {image && <img src={image} className="fullscreen-image" alt="world" />}
        <div className="controls">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Enter a prompt"
            className="prompt-input"
          />
          <button onClick={handleSubmit} disabled={loading} className="send-button">
            {loading ? 'Generating...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
