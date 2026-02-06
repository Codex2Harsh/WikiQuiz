from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from database import Base

class QuizHistory(Base):
    __tablename__ = "quiz_history"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=False, index=True)
    topic = Column(String)
    full_json_response = Column(JSON) 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())