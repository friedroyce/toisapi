from fastapi import FastAPI
from .routes import snipe_router

app = FastAPI()

app.include_router(snipe_router)
