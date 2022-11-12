from ...configurations.database.models.city import City
from typing import List, Optional

CITIES = [
    City(id=1, name="Medellin", description="Ciudad de la eterna primavera", tourist_annual_count=676652)
]


def get_cities() -> List[City]:
    return CITIES

def get_city(city_id: int) -> Optional[City]:
    for city in CITIES:
        if city.id == city_id:
            return city

    return None