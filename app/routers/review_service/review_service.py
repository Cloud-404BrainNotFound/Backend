from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.review import Review
from app.database import get_db

review_router = APIRouter()