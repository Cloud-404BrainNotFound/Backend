from passlib.context import CryptContext

# 创建密码上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 使用密码上下文来哈希一个密码
hashed_password = pwd_context.hash("hashed_password")

# 打印哈希后的密码
print(hashed_password)