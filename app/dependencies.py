"""Example dependencies"""

from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")  # pragma: no cover


async def get_query_token(token: str):
    if token != "morty":
        raise HTTPException(status_code=400, detail="No Morty token provided")  # pragma: no cover
    