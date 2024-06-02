from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class get_user_code(BaseModel):
    mail: EmailStr

