from config import supabase
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

    def __str__(self) -> str:
        return f'User: {self.name}'
    
    def __repr__(self) -> str:
        return f'User: {self.name}'
    
    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.email == other.email and self.password == other.password

    @staticmethod
    def get_all_users() -> List[object]:
        users = supabase.table('users').select('*').execute()
        return users
    
    @staticmethod
    def get_user_by_id(id: int) -> object:
        try:
            user = supabase.table('users').select('*').eq('id', id).single().execute()
            return user
        except Exception as e:
            return {'error': 500, 'data': 'User not exist'}
    
    @staticmethod
    def create_user(user: object) -> object:
        user = supabase.table('users').insert({'name': user.name, 'email': user.email, 'password': user.password}).execute()
        return user
    
    @staticmethod
    def update_user(id: int, user: object) -> object:
        new_user = supabase.table('users').update({'name': user.name, 'email': user.email, 'password': user.password}).eq('id', id).execute()
        if not new_user.data:
            return {'error': 500, 'data': 'User not exist'}
        return new_user
    
    @staticmethod
    def delete_user(id: int) -> object:
        delete_user = supabase.table('users').delete().eq('id', id).execute()
        
        if not delete_user.data:
            return {'error': 500, 'data': 'User not exist'}

        return delete_user