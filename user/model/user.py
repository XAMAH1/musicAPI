from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr

class new_user(BaseModel):
    nickname: Annotated[str, MinLen(3), MaxLen(30)]
    fio: Annotated[str, MinLen(3), MaxLen(40)]
    mail: EmailStr
    age: str = "27.10.2004"
    phone: Annotated[str, MinLen(8), MaxLen(20)]
    password: str
    user_code: str = "424823"

