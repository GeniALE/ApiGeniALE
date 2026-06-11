from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from app.db.models.members import Member
from app.db.models.departments import Departement

class Geniale(SQLModel, table=True):
    __tablename__ = "geniale"
    
    id_geniALE: UUID = Field(default=None, primary_key=True, default_factory=uuid4)
    nom: str = Field(nullable=False)
    prenom: str = Field(nullable=False)
    linkedin: str =Field(nullable=False, unique=True)
    photo: str = Field(nullable=False)
    
    
    members: list["Member"] = Relationship(back_populates="geniALE", cascade_delete=True)
    departements: list["Departement"] = Relationship(back_populates="geniALE", cascade_delete=True)