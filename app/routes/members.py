from fastapi import APIRouter, HTTPException
from app.controllers import members
route = APIRouter(prefix="/members", tags=["members"])

# Données temporaires (à remplacer par une DB)
members_db = [
    {"id_membre": 1, "id_geniALE": 42, "id_departement": 3, "date_admission": "2024-09-01"},
    {"id_membre": 2, "id_geniALE": 43, "id_departement": 1, "date_admission": "2024-10-15"},
    {"id_membre": 3, "id_geniALE": 44, "id_departement": 2, "date_admission": "2024-11-20"},
]


@route.get("/")
async def get_members():
    """Liste tous les membres"""
    if not members_db:
        raise HTTPException(status_code=404, detail="No members found")
    return members.getMembers()
