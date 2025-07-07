from sqlalchemy import String, Text, Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "notes"

id: Mapped[int] = mapped_column(primary_key=True, index=True)
title: Mapped[str] = mapped_column(String(100), nullable=False)
content: Mapped[str] = mapped_column(Text, nullable=True)
created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), onupdate=func.now())