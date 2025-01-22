from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from passlib.context import CryptContext
from api.db.database import Base

# Initialize the passlib context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    # Primary Key
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )

    # User Details
    username = Column(String(150), unique=True, index=True, nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=True)

    # Authentication and Verification
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)  # To manage user suspension/activation
    is_verified = Column(Boolean, default=False)  # Email verification status

    # Role and Relationships
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)  # Link to roles
    role = relationship("Role", back_populates="users")

    # Timestamps
    last_sign_in = Column(DateTime, nullable=True)
    account_created_at = Column(DateTime, default=func.now())

    # Relationships with other tables
    carts = relationship(
        "Cart", back_populates="user", cascade="all, delete-orphan"
    )  # Link to user's cart

    # Password utilities
    def set_password(self, password: str):
        """Hash and set the user's password."""
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify the provided password against the hashed password."""
        return pwd_context.verify(password, self.password_hash)