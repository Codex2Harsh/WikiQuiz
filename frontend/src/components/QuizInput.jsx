import { useState } from 'react';

export default function QuizInput({ onGenerate, loading }) {
  const [url, setUrl] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (url) onGenerate(url);
  };

  return (
    <div className="card">
      <h2> A New Quiz</h2>
      <p style={{ color: '#64748b', marginBottom: '1rem' }}>
        Paste a Wikipedia link below to create a quiz instantly using AI.
      </p>
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          className="input"
          placeholder="https://en.wikipedia.org/wiki/Alan_Turing"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
        />
        <button type="submit" className="btn" disabled={loading}>
          {loading ? 'Generating...' : 'Generate Quiz'}
        </button>
      </form>
    </div>
  );
}