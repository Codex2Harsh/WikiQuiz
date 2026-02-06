import QuizResults from "./QuizResults";

export default function ResultModal({ data, onClose }) {
  if (!data) return null;

  return (
    <div style={{
      position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
      backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', 
      alignItems: 'center', zIndex: 1000, backdropFilter: 'blur(3px)'
    }}>
      <div style={{
        background: 'white', width: '90%', maxWidth: '800px', maxHeight: '90vh',
        overflowY: 'auto', borderRadius: '12px', padding: '20px', position: 'relative'
      }}>
        <button 
          onClick={onClose}
          style={{
            position: 'absolute', top: '15px', right: '15px',
            background: '#ef4444', color: 'white', border: 'none',
            borderRadius: '50%', width: '30px', height: '30px', cursor: 'pointer'
          }}
        >
          ✕
        </button>
        <QuizResults data={data} />
      </div>
    </div>
  );
}