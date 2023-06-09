from fastapi import APIRouter, HTTPException, Request
from models.Blog import Blog
from typing import List

router = APIRouter()

@router.get('')
async def get_all_blogs() -> object:
    try:
        blogs = Blog.get_all_blogs()

        return blogs
    except Exception as e:
        raise HTTPException(status_code=500, detail='Server Error: %s' % str(e))
    
@router.get('/{id}')
async def get_blog_by_id(id: int) -> object:
    try:
        blog = Blog.get_blog_by_id(id)

        return blog
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to get blog\n Error: %s' % str(e))

@router.get('/user/{id}')
async def get__all_user_blogs(id: int) -> object:
    try:
        blogs = Blog.get_all_blogs_by_user(id)

        return blogs
    except Exception as e:
        raise HTTPException(status_code=500, detail='Server Error: %s' % str(e))

@router.post('')
async def create_blog(blog: Blog) -> object:
    try:
        new_blog = Blog.create_blog(blog)

        return new_blog
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to create blog\n Error: %s' % str(e))

@router.put('/{id}')
async def update_blog(id: int, req: Request) -> object:
    try:
        old_blog = Blog.get_blog_by_id(id)

        if 'error' in old_blog:
            raise HTTPException(status_code=500, detail='Blog not exist')

        body = await req.json()
        blog = Blog.update_blog(id, Blog (
            title = body['title'] if 'title' in body else old_blog.data['title'],
            content = body['content'] if 'content' in body else old_blog.data['content'],
            user_id = body['user_id'] if 'user_id' in body else old_blog.data['user_id']
            )
        )
        return blog
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to update blog\n Error: %s' % str(e))

@router.delete('/{id}')
async def delete_blog(id: int) -> object:
    try:
        blog = Blog.delete_blog(id)
        return blog
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to delete blog\n Error: %s' % str(e))