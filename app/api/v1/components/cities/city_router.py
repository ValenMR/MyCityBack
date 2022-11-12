from fastapi import APIRouter, Path, HTTPException, status
from ..sectors.sector_logic import get_sectors_by_city
from .city_logic import get_cities, get_city
from ...configurations.database.models.city import City
from ...configurations.database.models.sector import Sector
from typing import List

router = APIRouter()


@router.get("/", response_model=List[City])
def get_cities_controller():
    return get_cities()



@router.get("/{city_id}", response_model=City)
def get_city_controller(city_id: int = Path(default=..., title="Unique city identifier")):
    city = get_city(city_id)

    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="City not found")

    return city

@router.get("/{city_id}/sectors", response_model=List[Sector])
def get_city_controller(city_id: int = Path(default=..., title="Unique city identifier")):
    city = get_city(city_id)

    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="City not found")

    return get_sectors_by_city(city_id)