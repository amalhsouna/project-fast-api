from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get('/blog')
def index(limit:int = 10, pulished:bool=True, sort:str = None):
    # only get 10 published blogs
    if pulished:
        return {'data': {'test': f'hello {limit}'}}
    else:
        return 'hello word'


@app.get('/blog/unpulished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comment(id: int):
    return {'comment' : {"1", "2" ,"3", "4"}}

class Blog(BaseModel):
    title: str
    descitpion: str

@app.post('/blog')
def create_blog(request: Blog):
    return request
    return {'data': "blog is created"}