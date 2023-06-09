from config import supabase
from typing import List, Dict, Union
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str
    user_id: int

    @staticmethod
    def get_all_blogs() -> List[object]:
        blogs = supabase.table('blogs').select('*').execute()
        return blogs
    
    def get_all_blogs_by_user(user_id: int) -> List[object]:
        blogs = supabase.table('blogs').select('*').eq('user_id', user_id).execute()
        return blogs

    @staticmethod
    def get_blog_by_id(id: int) -> object:
        try:
            blog = supabase.table('blogs').select('*').eq('id', id).single().execute()
            return blog
        except Exception as e:
            return {'error': 500, 'data': 'Blog not exist'}
        
    @staticmethod
    def get_blog_content(id: int) -> object:
        try:
            blog = supabase.table('blogs').select('content').eq('id', id).single().execute()
            return blog

        except Exception as e:
            return {'error': 500, 'data': 'Blog not exist'}

    @staticmethod
    def create_blog(blog: object) -> object:
        blog = supabase.table('blogs').insert({'title': blog.title, 'content': blog.content, 'user_id': blog.user_id}).execute()
        return blog

    @staticmethod
    def update_blog(id: int, blog: object) -> object:
        new_blog = supabase.table('blogs').update({'title': blog.title, 'content': blog.content, 'user_id': blog.user_id}).eq('id', id).execute()
        if not new_blog.data:
            return {'error': 500, 'data': 'Blog not exist'}
        return new_blog
    
    @staticmethod
    def delete_blog(id: int) -> object:
        delete_blog = supabase.table('blogs').delete().eq('id', id).execute()
        
        if not delete_blog.data:
            return {'error': 500, 'data': 'Blog not exist'}

        return delete_blog
    