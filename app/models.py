
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

# Keep your existing Base import
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    Completed: Mapped[bool] = mapped_column(Boolean, default=False)
