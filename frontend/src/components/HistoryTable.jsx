export default function HistoryTable({ history, onViewDetails }) {
  if (!history || history.length === 0) {
    return <div className="card">No history found. Generate a quiz first!</div>;
  }

  return (
    <div className="card">
      <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid #e2e8f0' }}>
            <th style={{ padding: '10px' }}>ID</th>
            <th style={{ padding: '10px' }}>Topic</th>
            <th style={{ padding: '10px' }}>URL</th>
            <th style={{ padding: '10px' }}>Action</th>
          </tr>
        </thead>
        <tbody>
          {history.map((item) => (
            <tr key={item.id} style={{ borderBottom: '1px solid #f1f5f9' }}>
              <td style={{ padding: '10px', color: '#64748b' }}>#{item.id}</td>
              <td style={{ padding: '10px', fontWeight: 'bold' }}>{item.title}</td>
              <td style={{ padding: '10px' }}>
                <a href={item.url} target="_blank" rel="noopener noreferrer" style={{ color: '#2563eb' }}>
                  Link ↗
                </a>
              </td>
              <td style={{ padding: '10px' }}>
                <button 
                  onClick={() => onViewDetails(item)}
                  style={{ 
                    padding: '5px 10px', 
                    background: '#e0f2fe', 
                    color: '#0284c7', 
                    border: 'none', 
                    borderRadius: '6px', 
                    cursor: 'pointer',
                    fontWeight: 'bold'
                  }}
                >
                  View Quiz
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}