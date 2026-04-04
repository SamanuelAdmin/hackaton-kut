import uvicorn
from fastapi import FastAPI

from .accounts import AccountsRouter, load_models
from .database import DatabaseConnection
from .configs import *
from .utils import DatabaseConnectionInterface


# database stuff
databaseConnector: DatabaseConnectionInterface = DatabaseConnection()
databaseConnector.init(
    host=configs["DATABASE_HOST"],
    port=configs["DATABASE_PORT"],
    user=configs["DATABASE_USER"],
    password=configs["DATABASE_PASSWORD"],
)
load_models(databaseConnector.engine)


app = FastAPI()

# including routers
app.include_router(AccountsRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:1337",
        "http://127.0.0.1:8000",
        "https://pets.xhosts.xyz",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host=configs["host"], port=configs["port"], reload=True)
