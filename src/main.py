import uvicorn
from fastapi import FastAPI

from configs import settings
from pets import PetsRouter

app = FastAPI()

# including routers
app.include_router(PetsRouter, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
