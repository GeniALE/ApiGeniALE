from fastapi import APIRouter
from app.controllers import members
route = APIRouter(prefix="/members", tags=["members"])


#===============================CRUD=================================

@route.get("/")
async def get_members():
    """Liste tous les membres"""

    return members.getMembers()
