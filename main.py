from fastapi import FastAPI
from api import blogRouter

app = FastAPI()

app.include_router(blogRouter.router)