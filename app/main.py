from fastapi import FastAPI
from .crud import articles,login,users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(articles.router)
app.include_router(login.router)
app.include_router(users.router)


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