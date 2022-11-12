from ...configurations.database.models.place import Place
from typing import List, Optional
from ...configurations.lexica.lexica import get_random_image

PLACES = [
    Place(
        id=1,
        name="Popular", 
        description="Ubicado en el extremo nororiental de la ciudad, es el barrio más pequeño",
        icon="home",
        sector_id=1,
    ),
    Place(
        id=2,
        name="Buenos Aires", 
        description="Uno de los sectores más tradicionales de Medellín, está ubicado al oriente de la ciudad, muy cerca al centro urbano",
        icon="pub",
        sector_id=2,
        open="18:00 hrs",
        close="05:00 hrs"
    ),
    Place(
        id=3,
        name="Poblado", 
        description="Es la comuna más grande. Antiguamente era una zona conformada por fincas de grandes extensiones con cultivos frutales",
        icon="pub",
        sector_id=3,
        open="18:00 hrs",
        close="05:00 hrs"
    ),
    Place(
        id=4,
        name="Doce de octubre", 
        description="Asentamiento caracterizado por viviendas dispersas a las que se accedía desde la carretera al Mar",
        icon="house",
        sector_id=4,
    ),
    Place(
        id=5,
        name="Laureles—Estadio", 
        description="Unidad deportiva atanasio girardot",
        icon="stadium",
        sector_id=5,
    ),
    Place(
        id=6,
        name="Belén", 
        description="Belén es hoy una zona de clase media emergente y de clase media alta",
        icon="house",
        sector_id=6,
    ),
]


def __map_image_to_place(sector: Place) -> Place:
    sector.image = get_random_image(sector.description.replace(" ", "_"))
    return sector

def get_places() -> List[Place]:
    return list(map(__map_image_to_place, PLACES))

def get_places_by_sector(sector_id: int) -> List[Place]:
    places = []

    for place in PLACES:
        if place.sector_id == sector_id:
            places.append(place)

    return list(map(__map_image_to_place, places))


def get_place(place_id: int) -> Optional[Place]:
    for place in PLACES:
        if place.id == place_id:
            place.image = get_random_image(place.description.replace(" ", "_"))
            return place

    return None
