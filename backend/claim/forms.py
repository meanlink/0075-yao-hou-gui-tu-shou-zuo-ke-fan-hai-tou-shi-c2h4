from datetime import date
from typing import Literal
from pydantic import BaseModel, Field

class Transfer(BaseModel):
    destination:str=Field(pattern=r"^[A-Z0-9-]{3,24}$")

class Arrival(BaseModel):
    studio:str=Field(pattern=r"^[A-Z0-9-]{3,24}$")
    decision:Literal["accepted","returned"]

class Claim(BaseModel):
    studio:str=Field(pattern=r"^[A-Z0-9-]{3,24}$")
    code:str=Field(pattern=r"^[A-Z0-9-]{3,24}$")
    receiver:str=Field(min_length=2,max_length=80)
    local_day:date
