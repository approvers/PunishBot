import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

CWD = os.getcwd()
DOTENV_PATH = os.path.join(CWD, ".env")

load_dotenv(DOTENV_PATH)


class PunishBotConfig(BaseSettings):
    DISCORD_TOKEN: str
    DISCORD_PUNISHMENT_TARGET_USER_ID: int