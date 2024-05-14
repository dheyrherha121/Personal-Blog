from fastapi import APIRouter, status, HTTPException, Depends
from .. import schema, model
from ..database import get_db
from sqlalchemy.orm import session

router = APIRouter(
    prefix= '/Articles',
    tags= ['Articles']
)

#@router.get(status_code=status.HTTP_200_OK)
#def get_all():
 #   return

@router.post('/', status_code=status.HTTP_200_OK, response_model=schema.Blogout)
def new_blog(blog: schema.Blogin, db: session= Depends(get_db)):

    new_blog= model.Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {blog}

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_article(id: int, db: session=Depends(get_db)):
    return 'me'