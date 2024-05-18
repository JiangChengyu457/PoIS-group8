from typing import List,Union
from sqlalchemy.orm import Session


import models

from sql.schemas import posts, users,nodes
#from schemas import posts, users,nodes

from typing import overload
from fastapi import HTTPException

get_posts(db, post_ids)