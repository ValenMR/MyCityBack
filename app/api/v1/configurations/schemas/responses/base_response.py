from pydantic import BaseModel, Field

class BaseResponse(BaseModel):
    message: str = Field(default=..., description="Message to inform request status")
    status_code: int = Field(default=..., description="HTTP response status code", alias="statusCode")