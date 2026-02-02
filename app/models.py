from pydantic import BaseModel
from datetime import date


class Membre(BaseModel):
    id_geniALE: int
    id_departement: int
    date_admission: date


class MemberResponse(Membre):
    id_membre: int
