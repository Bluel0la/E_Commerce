from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.db.database import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(255), unique=True, nullable=False)

    # Relationships
    users = relationship("User", back_populates="role")
