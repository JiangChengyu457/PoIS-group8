from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from fastapi import (
    Depends,
    FastAPI,
)

from typing import Annotated
from models.users import User
from dependencies import get_current_user,show_tags

from fakedb import fake_users_db

from routers import posts, users

app=FastAPI(
    title="失敗なし",
    description="""
    先輩たちからの経験談。
    """,
    version="0.0.1",
    
)

add_pagination(app)

origins=[
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)

# Not ready
@app.get("/",tags=["home"])
async def root(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        if not show_tags(fake_users_db,current_user):
            return RedirectResponse("/users/interest_tags")
        else:
            return {"message":"timeline of posts","detail":current_user}
    else:
        return RedirectResponse("/users/login")
