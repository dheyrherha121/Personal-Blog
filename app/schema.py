from pydantic import BaseModel


class Blogin(BaseModel):
    title: str
    Text: str
    Article_number: int


class Blogout(BaseModel):
    title: str
    article_number: int


