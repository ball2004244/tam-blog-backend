from fastapi import FastAPI
from controllers import root_router, blog_router, user_router
app = FastAPI()

app.include_router(root_router)
app.include_router(blog_router, prefix='/blog')
app.include_router(user_router, prefix='/user')