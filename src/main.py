from fastapi import FastAPI

from src.pets import AccountsRouter


app = FastAPI()

# including routers
app.include_router(AccountsRouter)
