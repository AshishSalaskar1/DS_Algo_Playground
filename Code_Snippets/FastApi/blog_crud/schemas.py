from pydantic import BaseModel
from typing import Union, Optional

class BlogItem(BaseModel):
    title: str
    body: str
    published: Optional[bool]