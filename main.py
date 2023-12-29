from fastapi import FastAPI

from db import models
from db.database import engine
from router import user


app = FastAPI()
app.include_router(user.router)

@app.get("/")
def root():
    return {'message':'this is my home page'}

models.Base.metadata.create_all(engine)