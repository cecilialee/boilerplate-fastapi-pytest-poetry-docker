from fastapi import APIRouter, Depends, FastAPI

from app.config import settings
from app.dependencies import get_query_token, get_token_header
from app.routers import items, users


# Instantiate entry point
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    dependencies=[Depends(get_query_token)],
)

# Include routers from modules
api_router = APIRouter()
api_router.include_router(items.router)
api_router.include_router(users.router)

app.include_router(api_router, prefix=settings.API_V1_STR)
