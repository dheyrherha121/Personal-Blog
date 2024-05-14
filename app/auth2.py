from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from .config import setting


oauth2 = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = setting.secret_key
EXPIRE_MINUTE = setting.expire_minutes
ALGORITHM = setting.algorithm

def create_acces_token(data: dict):

    #to add the expiration minutes to the token head
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(EXPIRE_MINUTE)
    to_encode.update({'exp': expires})
    
    #to encode the token details
    




