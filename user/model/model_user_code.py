from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr

class m_user_code(BaseModel):
    mail: EmailStr
    user_code: str = "312543"

