from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class user_autme(BaseModel):
    mail: EmailStr
    os: str
    name_device: str
    version_program: str
    password: str


