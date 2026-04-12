import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Request

from src.configs import settings
from src.pets.router import router as PetsRouter
from src.pets.exceptions import NoEntityByIdFound

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:1338",
        "http://127.0.0.1:8000",
        "https://pets.xhosts.xyz",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# including routers
app.include_router(PetsRouter)


@app.exception_handler(NoEntityByIdFound)
async def not_found_entity_error_handler(request: Request, exc: NoEntityByIdFound):
    raise HTTPException(404, "Not found entity by id.")


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
