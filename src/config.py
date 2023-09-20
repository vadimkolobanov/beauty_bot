from dataclasses import dataclass
from os import environ


@dataclass
class Config:
    token: str = environ.get('TOKEN', 'define me!')
    admin_id: int = environ.get('ADMIN_IDS', 'define me!')
