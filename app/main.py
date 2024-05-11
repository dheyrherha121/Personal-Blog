from fastapi import FastAPI
from .crud import articles

app = FastAPI()
app.include_router(articles.router)

@app.get('/')
def index():
    return {'welcome to my personal blog❤️'}