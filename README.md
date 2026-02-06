# 🧠 WikiQuiz App

A full-stack application that automatically generates interactive quizzes from any Wikipedia article using AI.
[🚀 **View Live App**](https://wikiquiz-frontend.onrender.com)

## 🛠️ Tech Stack

**Frontend**
* **Framework:** React + Vite
* **Styling:** Minimal CSS (Clean UI)
* **HTTP Client:** Axios

**Backend**
* **Framework:** FastAPI (Python)
* **Database:** PostgreSQL (SQLAlchemy ORM)
* **AI Integration:** LangChain + Google Gemini API
* **Scraping:** BeautifulSoup4

---

## ✨ Features

### 1. 🚀 Generate Quiz (Tab 1)
* **Instant Scraping:** Extracts clean text from any valid Wikipedia URL.
* **AI-Powered Generation:** Uses Gemini LLM to create 5 distinct questions (Easy/Medium/Hard).
* **Structured Output:** Displays a summary, key entities (People, Locations), and related topics.
* **Interactive Mode:** "Reveal Answers" button to test your knowledge dynamically.

### 2. 📜 Past Quizzes (Tab 2)
* **History Tracking:** All generated quizzes are automatically saved to the PostgreSQL database.
* **Dashboard:** View a table of all previously generated topics.
* **Details Modal:** Re-open any past quiz in a popup without regenerating it.

---

## ⚙️ How to Run Locally

Follow these steps to set up the project on your machine.

### Prerequisites
* Node.js & npm
* Python 3.10+
* PostgreSQL (Running on Port `5321`)
* Google Gemini API Key

### 1. Database Setup
Create a new database named `wikiquiz` in PostgreSQL.
```sql
CREATE DATABASE wikiquiz;
```
### 2. Backend Setup
Navigate to the backend folder and install dependencies.
```
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv
# Activate: source venv/bin/activate (Mac/Linux) or venv\Scripts\activate (Windows)

# Install required libraries
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic beautifulsoup4 requests langchain-google-genai langchain langchain-community

# Create .env file
# NOTE: Replace 'yourpassword' and 'your_key' with actual values
echo "DATABASE_URL=postgresql://postgres:yourpassword@localhost:5321/wikiquiz" > .env
echo "GOOGLE_API_KEY=your_gemini_api_key_here" >> .env
Run the Server:

Bash
uvicorn main:app --reload --port 8000
```
3. Frontend Setup
Open a new terminal, navigate to the frontend folder, and start the UI.

```
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
Open your browser and visit: http://localhost:5173
```
Project Screenshot:
<img width="1362" height="943" alt="image" src="https://github.com/user-attachments/assets/0f3cb95b-edab-4d92-bb34-7cbf21a2c05f" />
<img width="1116" height="491" alt="image" src="https://github.com/user-attachments/assets/13b5abf7-d8b4-4f44-8eed-076bc1dae0c7" />

