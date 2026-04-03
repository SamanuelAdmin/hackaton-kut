from fastapi import APIRouter
from src.accounts.service import UserService
from src.schemas import AuthDTO, JWTToken, RegistrationDTO

from src.configs import configs

router = APIRouter(prefix="/accounts", tags=["accounts", "account"])
user_service = UserService(configs["JWT_PRIVATE_KEY"])


@router.get("/create")
async def register(registerDTO: RegistrationDTO) -> JWTToken:
    return user_service.create(registerDTO)


@router.get("/auth")
async def auth(authDTO: AuthDTO) -> JWTToken:
    return user_service.auth(authDTO)
