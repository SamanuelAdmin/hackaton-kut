from fastapi import APIRouter


router = APIRouter(prefix="/pets", tags=["pets", "account"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
