from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from .config import setting
from jose import jwt, JWTError
from .schema import TokenData


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
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encode_jwt

def verify_token(token:str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get('user_id')
        if id is None:
            raise credential_exception
        token_data = TokenData(id = id)

    except JWTError:
        raise credential_exception
    
    return token_data




