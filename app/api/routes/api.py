from fastapi import APIRouter
from app.api.routes import institutions

router = APIRouter()

router.include_router(institutions.router,
                      tags=["institutions"],
                      prefix="/institutions")
