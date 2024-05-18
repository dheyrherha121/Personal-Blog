from  fastapi import HTTPException
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#to hash the input password
def hash(password: str):
    pwd_context.hash(password)

def verify(plain_password, hashed_password):
    pwd_context.verify(plain_password, hashed_password)
    