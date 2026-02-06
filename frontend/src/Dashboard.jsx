import { useState, useEffect } from 'react';
import axios from 'axios';
import QuizInput from './components/QuizInput';
import QuizResults from './components/QuizResults';
import HistoryTable from './components/HistoryTable';
import ResultModal from './components/ResultModal';

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('generate'); 
  const [loading, setLoading] = useState(false);
  const [currentQuiz, setCurrentQuiz] = useState(null);
  const [history, setHistory] = useState([]);
  const [modalData, setModalData] = useState(null);
  const handleGenerate = async (url) => {
    setLoading(true);
    setCurrentQuiz(null);
    try {
      const res = await axios.post('http://127.0.0.1:8000/generate', { url });
      console.log("AI Response Data:", res.data);
      setCurrentQuiz(res.data);
    } catch (error) {
      alert("Error generating quiz. Check console/backend.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const fetchHistory = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/history');
      setHistory(res.data);
    } catch (error) {
      console.error("Error fetching history:", error);
    }
  };

  useEffect(() => {
    if (activeTab === 'history') {
      fetchHistory();
    }
  }, [activeTab]);

  return (
    <div className="container">
      <header style={{ marginBottom: '2rem', textAlign: 'center' }}>
        <h1>🧠 WikiQuiz AI</h1>
        <p style={{ color: '#64748b' }}>Turn any Wikipedia article into a quiz instantly.</p>
      </header>

      <div className="tabs">
        <div 
          className={`tab ${activeTab === 'generate' ? 'active' : ''}`}
          onClick={() => setActiveTab('generate')}
        >
          Generate Quiz
        </div>
        <div 
          className={`tab ${activeTab === 'history' ? 'active' : ''}`}
          onClick={() => setActiveTab('history')}
        >
          Past Quizzes
        </div>
      </div>

      {activeTab === 'generate' && (
        <>
          <QuizInput onGenerate={handleGenerate} loading={loading} />
          {loading && <div className="loader">✨ AI is reading the article and crafting questions...</div>}
          {currentQuiz && <QuizResults data={currentQuiz} />}
        </>
      )}

      {activeTab === 'history' && (
        <HistoryTable history={history} onViewDetails={(item) => setModalData(item)} />
      )}

      {modalData && (
        <ResultModal data={modalData} onClose={() => setModalData(null)} />
      )}
    </div>
  );
}