from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.database import get_db

notification_router = APIRouter()