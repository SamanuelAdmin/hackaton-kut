# .env and configs parser

import hashlib
import os
from dotenv import load_dotenv
from src.utils import Singleton


load_dotenv()


class Configs(dict, Singleton):
    pass


configs: dict[str, int | str] = {}
configs.update(os.environ)

# load jwt secret key
with open("../jwt.private") as jwt_private_file:
    configs["JWT_PRIVATE_KEY"] = jwt_private_file.read()
