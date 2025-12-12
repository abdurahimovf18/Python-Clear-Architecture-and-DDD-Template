from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.framework.container import Container


class Loader:

    def __init__(self):
        self.container = Container()

    @asynccontextmanager
    async def lifespan(self, fastapi_app: FastAPI) -> AsyncGenerator[None, None]:
        self.container.register_singleton(FastAPI, fastapi_app)

        yield
