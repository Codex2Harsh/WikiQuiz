from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import models, schemas
from database import engine, get_db
from services.scraper import scrape_wikipedia
from services.llm import generate_quiz_content

# Ensure all database tables are created when the app starts.
# This is convenient for development; in production you might use migrations instead.
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI application instance
app = FastAPI()

# Enable Cross-Origin Resource Sharing (CORS)
# This allows frontend apps (React, Next.js, etc.) running on different domains
# to communicate with this API without being blocked by the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=schemas.WikiQuizResponse)
def generate_quiz(request: dict, db: Session = Depends(get_db)):
    url = request.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
# Step 1: Scrape Wikipedia content
    scraped_data = scrape_wikipedia(url)

    # If scraping fails, stop and return a clear error
    if not scraped_data:
        raise HTTPException(status_code=400, detail="Failed to scrape Wikipedia page")

    try:
        # Step 2: Generate quiz using the LLM service
        quiz_data = generate_quiz_content(scraped_data['text'], url)
    except Exception as e:
        # Catch any AI/LLM-related errors and return a proper API response
        raise HTTPException(status_code=500, detail=str(e))

    # Step 3: Store quiz result in database for history tracking
    db_record = models.QuizHistory(
        url=url,
        topic=quiz_data.title,
        full_json_response=quiz_data.model_dump() 
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return quiz_data

@app.get("/history", response_model=List[schemas.QuizHistoryBase])
def get_history(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    history = db.query(models.QuizHistory).offset(skip).limit(limit).all()
    results = []
    for item in history:
        data = item.full_json_response
        data['id'] = item.id 
        results.append(data)
        
    return results