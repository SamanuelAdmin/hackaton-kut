from fastapi import APIRouter


router = APIRouter(prefix="/accounts", tags=["accounts", "account"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
