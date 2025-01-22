from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship
from api.db.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(255), unique=True, nullable=False)
    num_items = Column(Integer, CheckConstraint("num_items >= 0"), default=0)

    # Relationships
    items = relationship("Item", back_populates="category")
