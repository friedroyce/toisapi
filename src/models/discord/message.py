from datetime import datetime
from typing import List
from pydantic import BaseModel
from .user import User
from .attachment import Attachment
from .embed import Embed

class Message(BaseModel):
    id: str
    channel_id: str
    author: User
    content: str
    timestamp: datetime
    edited_timestamp: datetime
    tts: bool
    mention_everyone: bool
    mentions: List[str]
    attachments: List[Attachment]
    embeds: List[Embed]
