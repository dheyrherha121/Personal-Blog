from fastapi import APIRouter, status, HTTPException
from .. import schema

router = APIRouter(
    prefix= '/Articles',
    tags= ['Articles']
)

#@router.get(status_code=status.HTTP_200_OK)
#def get_all():
 #   return

@router.post('/', status_code=status.HTTP_200_OK)
def new_blog(blog: schema.Blogin):
    return {'your blog has been created successfully'}