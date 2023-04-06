from typing import Optional
from pydantic import BaseModel

class Attachment(BaseModel):
    id: str
    filename: str
    description: Optional[str]
    content_type: Optional[str]
    size: int
    url: str
    proxy_url: str
    height: Optional[int]
    width: Optional[int]
    ephemeral: Optional[bool]
