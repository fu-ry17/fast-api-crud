from typing import List

from db.db_setup import get_db
from db.models.blogModel import Blog
from fastapi import APIRouter, Depends, HTTPException, status
from schema import blog_schema
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

router = APIRouter()

@router.get('/', response_model=List[blog_schema.ResponseBlog])
async def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@router.post('/', response_model=blog_schema.ResponseBlog)
async def create_blog(blog: blog_schema.CreateBlog, db: Session = Depends(get_db)):
    new_blog = Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@router.get('/{id}', response_model=blog_schema.ResponseBlog)
async def get_single_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no blog was found with id {id}")

    return blog

@router.patch('/{id}', response_model=blog_schema.ResponseBlog)
async def update_blog(id: int, blog: blog_schema.CreateBlog, db: Session = Depends(get_db)):
    blog_query = db.query(Blog).filter(Blog.id == id)

    if blog_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no blog was found with id {id}")

    blog_query.update(blog.dict(), synchronize_session=False)
    db.commit()

    return blog_query.first()

@router.delete('/{id}')
async def delete_blog(id: int, db: Session = Depends(get_db)):
    blog_query = db.query(Blog).filter(Blog.id == id)

    if blog_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no post was found")
     
    blog_query.delete(synchronize_session=False)
    db.commit()

    return { "message": "delete succesful.."}