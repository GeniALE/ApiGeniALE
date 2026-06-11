"""The members module defines the Member model for the database."""
from sqlalchemy import Date
from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4
from app.db.models.departements import Departement
from app.db.models.geniales import Geniale

class Member(SQLModel, table=True):
    __tablename__ = "members"
    
    id_membre: UUID = Field(default=None, primary_key=True, default_factory=uuid4)
    id_geniALE: UUID = Field(nullable=False, foreign_key="geniales.id_geniALE")
    id_departement: UUID = Field(nullable=False, foreign_key="departements.id_departement")
    date_admission: Date = Field(nullable=False)
    date_depart: Date | None = Field(nullable=True)
    
    departement: list["Departement"] = Relationship(back_populates="members", cascade_delete=True)
    geniALE: list["Geniale"] = Relationship(back_populates="members", cascade_delete=True)