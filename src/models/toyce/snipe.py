from datetime import datetime
from typing import List
from pydantic import BaseModel
from ..discord import Message
from ..discord import User

class Snipe(BaseModel):
    id: str
    message: Message
    deleted_by: User
    timestamp: datetime = datetime.now()
