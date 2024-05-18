from fastapi import APIRouter, HTTPException,status,Depends
from sqlalchemy.orm import session
from ..database import get_db
from .. import model,schema, utility

router = APIRouter(
    prefix= '/users',
    tags=['users']
)

@router.post('/', status_code=status.HTTP_200_OK)
def create_user(user:schema.UserIn, db:session = Depends(get_db)):
    hashed_password = utility.hash(user.password)
    user.password = hashed_password

    new_user = model.User(user.dict())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {'welcome!! You can start creating your blogs❤️🙈'}


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.UserOut)
def get_user_by_id(id: int, db: session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
     
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f'User with id {id} not found')
    return user