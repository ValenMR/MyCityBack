from pydantic import BaseModel, Field
from typing import Optional

class City(BaseModel):
    id: int = Field(default=..., description="Unique city idenfier")
    name: str = Field(default=..., description="City name", max_length=255, min_length=4)
    description: Optional[str] = Field(default=None, description="Main city purpose", max_length=500)
    tourist_annual_count: int = Field(default=..., description="Number of tourist per year", gt=0)