from dataclasses import dataclass
from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
@dataclass
class Config:
    token: str = environ.get('TOKEN', 'define me!')
    admin_id: int = environ.get('ADMIN_IDS', 'define me!')
