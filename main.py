from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.database import engine
from router import user, post, comment
from auth import authentication


app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

@app.get("/")
def root():
    return {'message':'this is my home page'}


# adding cors by using middleware 
origins= [
    'http://lcoalhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =['*'],
    allow_headers = ['*']
)



models.Base.metadata.create_all(engine)

app.mount('/images',StaticFiles(directory='images'),name='images')