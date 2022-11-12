from fastapi import APIRouter, Path, HTTPException, status
from .sector_logic import get_sectors, get_sector
from ..places.place_logic import get_places_by_sector
from ...configurations.database.models.sector import Sector
from ...configurations.database.models.place import Place
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Sector])
def get_sectors_controller():
    return get_sectors()



@router.get("/{sector_id}", response_model=Sector)
def get_sector_controller(sector_id: int = Path(default=..., title="Unique sector identifier")):
    sector = get_sector(sector_id)

    if not sector:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sector not found")

    return sector


@router.get("/{sector_id}/places", response_model=List[Place], response_model_exclude_none=True)
def get_sector_places_controller(sector_id: int = Path(default=..., title="Unique sector identifier")):
    sector = get_sector(sector_id)

    if not sector:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sector not found")

    return get_places_by_sector(sector_id)