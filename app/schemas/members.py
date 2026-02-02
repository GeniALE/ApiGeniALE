from pydantic import BaseModel
from datetime import date

class Member(BaseModel):
    id_geniALE: int
    id_departement: int
    date_admission: date
    

class CreateMember(Member):
    name : str