from pydantic import BaseModel, Field
from typing import Optional

class Place(BaseModel):
    id: int = Field(default=..., description="Unique pkace idenfier")
    name: str = Field(default=..., description="Place name", max_length=255, min_length=4)
    description: Optional[str] = Field(default=None, description="Main city purpose", max_length=500)
    sector_id: int = Field(default=..., description="Unique sector identifier", gt=0)
    icon: str = Field(default=..., description="Icon uri image", max_length=255)
    open: Optional[str] = Field(default=None, description="Open hour")
    close: Optional[str] = Field(default=None, description="Open hour")
    image: Optional[str] = Field(default=None, description="Autogenerated image")