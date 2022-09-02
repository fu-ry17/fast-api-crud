from pydantic import BaseModel
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    description: str
    published: bool

class CreateBlog(BlogBase):
    pass

class ResponseBlog(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode =True
    