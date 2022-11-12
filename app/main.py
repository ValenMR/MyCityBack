from fastapi import FastAPI, status
from .api.v1.configurations.schemas.responses.base_response import BaseResponse
from .api.v1.routes import router as v1_router

app = FastAPI(
    title="My city"
)

@app.get("/", response_model=BaseResponse, response_model_exclude_none=True)
def main_root():
    """
    Return basic welcome message
    """
    return BaseResponse(
        message="Hello from My city Backend",
        statusCode=status.HTTP_200_OK
    )


app.include_router(v1_router, prefix="/api/v1")
