from fastapi import APIRouter
from .components.cities.city_router import router as city_router
from .components.sectors.sector_router import router as sector_router
from .components.places.place_router import router as place_router

router = APIRouter()


router.include_router(city_router, prefix="/cities", tags=["City"])
router.include_router(sector_router, prefix="/sectors", tags=["Sector"])
router.include_router(place_router, prefix="/places", tags=["Place"])