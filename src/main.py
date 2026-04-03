from fastapi import FastAPI

from src.accounts import AccountsRouter, load_models
from src.database import DatabaseConnection
from src.configs import *
from src.utils import DatabaseConnectionInterface


# database stuff
databaseConnector: DatabaseConnectionInterface = DatabaseConnection(
    host=configs["DATABASE_HOST"],
    port=configs["DATABASE_PORT"],
    user=configs["DATABASE_USER"],
    password=configs["DATABASE_PASSWORD"],
)
load_models(databaseConnector.engine)


app = FastAPI()

# including routers
app.include_router(AccountsRouter)
