from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import engine, get_db
from app.models import review, user, order, payment, notification  # 导入所有模型
from app.routers.user_service import user_router  # 导入用户相关的 router
from app.routers.review_service import review_router  # 导入评论相关的 router
from app.routers.order_service import order_router  # 导入订单相关的 router
from app.routers.payment_service import payment_router  # 导入支付相关的 router
from app.routers.notification_service import notification_router  # 导入通知相关的 router


# 创建数据库表
review.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)
payment.Base.metadata.create_all(bind=engine)
notification.Base.metadata.create_all(bind=engine)


app = FastAPI()


# 这是一个router的示例
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(review_router, prefix="/reviews", tags=["reviews"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
app.include_router(payment_router, prefix="/payments", tags=["payments"])
app.include_router(notification_router, prefix="/notifications", tags=["notifications"])


@app.get("/")
def read_root():
    return {"Hello": "World"}