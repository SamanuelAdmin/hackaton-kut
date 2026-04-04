import uvicorn
from fastapi import FastAPI

from configs import settings
from pets import PetsRouter

app = FastAPI()

# including routers
app.include_router(PetsRouter)

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

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
