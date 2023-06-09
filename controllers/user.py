from fastapi import APIRouter, HTTPException, Request
from models.User import User
from typing import List
router = APIRouter()

@router.get('')
async def get_all_users() -> object:
    try:
        users = User.get_all_users()
        return users
    
    except Exception as e:
        raise HTTPException(status_code=500, detail='Server Error: %s' % str(e))
    
@router.get('/{id}')
async def get_user_by_id(id: int) -> object:
    try:
        user = User.get_user_by_id(id)
        return user
    
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to get user\n Error: %s' % str(e))
    
@router.post('')
async def create_user(user: User) -> object:
    try:
        new_user = User.create_user(user)
        
        return new_user
    
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to create user\n Error: %s' % str(e))

@router.put('/{id}')
async def update_user(id: int, req : Request) -> object:
    try:
        old_user = User.get_user_by_id(id)

        if 'error' in old_user:
            raise HTTPException(status_code=500, detail='User not exist')
        
        body = await req.json()
        user = User.update_user(id, User (
            name = body['name'] if 'name' in body else old_user.data['name'],
            email = body['email'] if 'email' in body else old_user.data['email'],
            password = body['password'] if 'password' in body else old_user.data['password']
            )
        )
        return user
    
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to update user\n Error: %s' % str(e))
    
@router.delete('/{id}')
async def delete_user(id: int) -> object:
    try:
        user = User.delete_user(id)
        return user
    
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to delete user\n Error: %s' % str(e))
    