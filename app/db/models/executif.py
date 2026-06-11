"""The executif table defines the Executif model for the database."""
from sqlalchemy import Date
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4

class Executif(SQLModel, table=True):
    __tablename__ = "executifs"
    id_executif: UUID = Field(primary_key=True, default_factory=uuid4)
    id_membre: UUID = Field(nullable=False, foreign_key="members.id_membre")
    id_fonction: UUID = Field(nullable=False, foreign_key="fonctions.id_fonction")
    date_debut: Date = Field(nullable=False)
    date_fin: Date | None = Field(nullable=True)