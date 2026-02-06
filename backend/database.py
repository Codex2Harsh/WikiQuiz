from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
# Load environment variables from .env file so our secrets
# (like database credentials) are not hardcoded in the source code
load_dotenv()

# Read the database connection string from environment variables
# Example format:
# postgresql://user:password@localhost:5432/mydatabase
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create the core database engine.
# This is SQLAlchemy’s main interface to the actual database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory.
# Each time we call SessionLocal(), we get a new database session.
# - autocommit=False: we control when changes are saved
# - autoflush=False: prevents unexpected automatic database writes
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()