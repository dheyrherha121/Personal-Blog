from pydantic import BaseModel
from pydantic import EmailStr

class Blogin(BaseModel):
    title: str
    content: str
    Article_number: int


class Blogout(BaseModel):
    id: int
    title: str
    article_number: int

class TokenData(BaseModel):
    id: int

class UserIn(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class config:
       orm_mode= True