from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import session
from ..database import get_db
from .. import model, utility, auth2


router = APIRouter(
    prefix= '/login',
    tags= ['login']
)

@router.post('/')
def login(input_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: session= Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == input_data.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    if not utility.verify(input_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    
    token = auth2.create_acces_token(data =  {'user_id' : user.id})
    return {'token generated':token, 'token_type': 'Bearer'}
        