from fastapi import FastAPI

app = FastAPI()

@app.get()
def index():
    return {'welcome to my personal blog❤️'}