from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}