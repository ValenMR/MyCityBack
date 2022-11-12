from ...configurations.database.models.sector import Sector
from typing import List, Optional
from ...configurations.lexica.lexica import get_random_image

SECTORS = [
    Sector(id=1,name="Nororiental",description="Zona nororiental de Medellin",population=428000,city_id=1),
    Sector(id=2,name="Centroriental",description="Zona centroriental de Medellin",population=212000,city_id=1),
    Sector(id=3,name="Suroriental",description="Zona suroriental de Medellin",population=314000,city_id=1),
    Sector(id=4,name="Noroccidental",description="Zona noroccidental de Medellin",population=98000,city_id=1),
    Sector(id=5,name="Centroccidental",description="Zona centroccidental de Medellin",population=534000,city_id=1),
    Sector(id=6,name="Suroccidental",description="Zona suroccidental de Medellin",population=436000,city_id=1),
    
]

def __map_image_to_sector(sector: Sector) -> Sector:
    sector.image = get_random_image(sector.description.replace(" ", "_"))
    return sector

def get_sectors() -> List[Sector]:
    return list(map(__map_image_to_sector, SECTORS))

def get_sectors_by_city(city_id: int) -> List[Sector]:
    sectors = []

    for sector in SECTORS:
        if sector.city_id == city_id:
            sectors.append(sector)

    return list(map(__map_image_to_sector, sectors))


def get_sector(sector_id: int) -> Optional[Sector]:
    for sector in SECTORS:
        if sector.id == sector_id:
            sector.image = get_random_image(sector.description.replace(" ", "_"))
            return sector

    return None

