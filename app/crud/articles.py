from fastapi import APIRouter, status, HTTPException, Depends
from .. import schema, model, auth2
from ..database import get_db
from sqlalchemy.orm import session

router = APIRouter(
    prefix= '/Articles',
    tags= ['Articles']
)


@router.post('/', status_code=status.HTTP_200_OK, response_model=schema.Blogout)
def new_blog(blog: schema.Blogin, db: session= Depends(get_db), current_user: int = Depends(auth2.get_current_user)):

    new_blog= model.Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {blog}


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model= schema.Blogout)
def get_one_article(id: int, db: session=Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='the blog you are looking for does not exist')
    return blog

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, blog: schema.Blogin, db: session = Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    updated = blog.first()
    if not updated:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='the post you want to update does not exist')
    if updated.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Your are not the owner of the post you want to update 😒')
    blog.update(blog.dict(), synchronize_session=False)
    db.commit()

    return {'update successfull': blog.first()}

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: session= Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    deleted = blog.first()
    if not deleted:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='the post you want to update does not exist')
    if deleted.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Your are not the owner of the post you want to update 😒')
    blog.delete(synchronize_session=False)
    db.commit()

    return {'your post has been successfully deleted😒'}

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model= schema.Blogout)
def get_one_blog(id: int, db:session = Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='the blog you are looking for those not exist')
    return blog

