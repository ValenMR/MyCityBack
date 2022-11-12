from fastapi import APIRouter, Path, HTTPException, status
from .place_logic import get_places, get_place
from ...configurations.database.models.place import Place
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Place], response_model_exclude_none=True)
def get_places_controller():
    return get_places()



@router.get("/{place_id}", response_model=Place, response_model_exclude_none=True)
def get_place_controller(place_id: int = Path(default=..., title="Unique place identifier")):
    place = get_place(place_id)

    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Place not found")

    return place