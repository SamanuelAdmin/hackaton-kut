from fastapi import APIRouter, HTTPException
from .service import UserService
from .exceptions import IncorrectPassword, IncorrectValue, UserNotFound
from src.schemas import AuthDTO, JWTToken, RegistrationDTO

from src.configs import configs

router = APIRouter(prefix="/accounts", tags=["accounts", "account"])
user_service = UserService(configs["JWT_PRIVATE_KEY"])


@router.post("/create")
async def register(registerDTO: RegistrationDTO) -> JWTToken:
    try:
        jwt_token = user_service.create(registerDTO)
    except IncorrectValue:
        raise HTTPException(status_code=403, detail="Incorrect entered data.")

    return jwt_token


@router.post("/auth")
async def auth(authDTO: AuthDTO) -> JWTToken:
    try:
        jwt_token = user_service.auth(authDTO)
    except IncorrectPassword:
        raise HTTPException(status_code=403, detail="Incorrect creds.")
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found.")

    return jwt_token
