from fastapi import FastAPI

from src.accounts import AccountsRouter


app = FastAPI()

# including routers
app.include_router(AccountsRouter)
