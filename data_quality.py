from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveInt

class Selling(BaseModel):
    email: EmailStr
    name: str
    quantity: PositiveInt
