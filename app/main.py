from fastapi import FastAPI
from .crud import articles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(articles.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return {'welcome to my personal blog❤️'}