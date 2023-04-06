from typing import List
from fastapi import APIRouter
from ..models import Snipe
from ..models import Message

snipe_router = APIRouter()

@snipe_router.post("/snipes")
async def save_snipe(message: Message):
    return {"snipe": message}

@snipe_router.get("/snipes")
async def get_snipes() -> List[Snipe]:
    return {"messages": ["snipes"]}
