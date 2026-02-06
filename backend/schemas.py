from pydantic import BaseModel
from typing import List, Dict

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str
    explanation: str
class WikiQuizResponse(BaseModel):
    url: str
    title: str
    summary: str
    key_entities: Dict[str, List[str]] 
    sections: List[str]
    quiz: List[QuizQuestion]
    related_topics: List[str]
class QuizHistoryBase(WikiQuizResponse):
    id: int
    
    class Config:
        from_attributes = True