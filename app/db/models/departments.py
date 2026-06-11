
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4
from app.db.models.members import Member

class Departments(SQLModel, table=True):
    __tablename__ = "departments"

    id_departements: UUID = Field(default=None, primary_key=True, default_factory=uuid4)
    name: str = Field(nullable=False, unique=True)
    description: str = Field(nullable=True)

    members: list["Member"] = Relationship(back_populates="department", cascade_delete=True)