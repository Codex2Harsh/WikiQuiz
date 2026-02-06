import { useState } from 'react';

export default function QuizResults({ data }) {

  const [showAnswers, setShowAnswers] = useState(false);

  if (!data) return <div>No data received.</div>;
  if (!data.quiz) return <div>Data received, but 'quiz' field is missing! Check console.</div>;
  return (
    <div className="results-container">

      <div className="card">
        <h1>{data.title}</h1>
        <p style={{ lineHeight: '1.6' }}>{data.summary}</p>

        <div style={{ marginTop: '1rem' }}>
          <h3>Key Topics</h3>
          {(data.key_entities.People || data.key_entities.people)?.map(p => (
            <span key={p} className="tag">👤 {p}</span>
          ))}
          {(data.key_entities.Locations || data.key_entities.locations)?.map(l => (
            <span key={l} className="tag">📍 {l}</span>
          ))}
        </div>
      </div>

      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>🧠 Knowledge Check</h2>
          <button
            className="btn"
            style={{ backgroundColor: showAnswers ? '#64748b' : '#22c55e', fontSize: '0.9rem' }}
            onClick={() => setShowAnswers(!showAnswers)}
          >
            {showAnswers ? 'Hide Answers' : 'Reveal Answers'}
          </button>
        </div>

        {data.quiz.map((q, index) => (
          <div key={index} style={{ marginBottom: '2rem', paddingBottom: '1rem', borderBottom: '1px solid #eee' }}>
            <p style={{ fontWeight: 'bold', fontSize: '1.1rem' }}>
              {index + 1}. {q.question}
              <span style={{ fontSize: '0.8rem', color: '#999', marginLeft: '10px' }}>({q.difficulty})</span>
            </p>

            <ul style={{ listStyle: 'none', padding: 0 }}>
              {q.options.map((opt, i) => (
                <li key={i} style={{
                  padding: '0.5rem',
                  marginBottom: '0.25rem',
                  borderRadius: '6px',
                  background: showAnswers && opt === q.answer ? '#dcfce7' : '#f1f5f9',
                  border: showAnswers && opt === q.answer ? '1px solid #86efac' : '1px solid transparent'
                }}>
                  {opt}
                </li>
              ))}
            </ul>

            {showAnswers && (
              <p style={{ fontSize: '0.9rem', color: '#64748b', fontStyle: 'italic' }}>
                💡 <strong>Explanation:</strong> {q.explanation}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}