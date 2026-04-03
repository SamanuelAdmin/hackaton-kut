from fastapi import FastAPI

from src.accounts import AccountsRouter
from src.database import DatabaseConnection
from src.configs import *


# database stuff
databaseConnector = DatabaseConnection(
    host=configs["DATABASE_HOST"],
    port=configs["DATABASE_PORT"],
    user=configs["DATABASE_USER"],
    password=configs["DATABASE_PASSWORD"],
)

app = FastAPI()

# including routers
app.include_router(AccountsRouter)
