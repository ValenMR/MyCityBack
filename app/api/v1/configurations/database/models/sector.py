from pydantic import BaseModel, Field
from typing import Optional

class Sector(BaseModel):
    id: int = Field(default=..., description="Unique sector idenfier")
    name: str = Field(default=..., description="sector name", max_length=255, min_length=4)
    description: Optional[str] = Field(default=None, description="Main sector purpose", max_length=500)
    population: int = Field(default=..., description="Current amount of people", gt=0)
    city_id: int = Field(default=..., description="Unique city identifier", gt=0)
    image: Optional[str] = Field(default=None, description="Image", max_length=255)