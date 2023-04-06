from datetime import datetime
from typing import List
from typing import Optional
from pydantic import BaseModel

class EmbedFooter(BaseModel):
    text: str
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]

class EmbedMedia(BaseModel):
    url: str
    proxy_url: Optional[str]
    width: Optional[int]
    height: Optional[int]

class EmbedProvider(BaseModel):
    name: Optional[str]
    url: Optional[str]

class EmbedAuthor(BaseModel):
    name: str
    url: Optional[str]
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]

class EmbedField(BaseModel):
    name: str
    value: str
    inline: Optional[bool]

class Embed(BaseModel):
    title: Optional[str]
    type: Optional[str]
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[datetime]
    color: Optional[int]
    footer: Optional[EmbedFooter]
    image: Optional[EmbedMedia]
    thumbnail: Optional[EmbedMedia]
    video: Optional[EmbedMedia]
    provider: Optional[EmbedProvider]
    author: Optional[EmbedAuthor]
    fields: Optional[List[EmbedField]]
