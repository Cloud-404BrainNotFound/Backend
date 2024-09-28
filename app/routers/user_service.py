from fastapi import APIRouter, Depends, HTTPException,Form
from sqlalchemy.orm import Session
from app.models.user import User
from app.database import get_db
from passlib.context import CryptContext

user_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@user_router.get("/first_user")
def get_first_user_id(db: Session = Depends(get_db)):
    first_user = db.query(User).first()

    if not first_user:
        raise HTTPException(status_code=404, detail="No user found")
    return {"id": first_user.id}

@user_router.get("/{username}")
def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.id, "username": user.username, "email": user.email}

@user_router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        # 用户不存在
        raise HTTPException(status_code=404, detail="User not found")
        # 先进行明文比较，之后再视情况启用哈希比较 
    elif (password is None) or(user.password != password):
        # 密码不匹配
        raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        # 登录成功
        return {"message": "Login successful", "user_id": user.id, "username": user.username}