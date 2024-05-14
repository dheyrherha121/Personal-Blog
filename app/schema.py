from pydantic import BaseModel


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

