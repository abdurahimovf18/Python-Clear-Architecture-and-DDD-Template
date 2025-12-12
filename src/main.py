from fastapi import FastAPI

from src.loader import Loader

__all__ = [
    "app",
]

loader = Loader()
app = FastAPI(lifespan=loader.lifespan)
