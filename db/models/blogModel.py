from sqlalchemy import Column, Integer, String, text, TIMESTAMP, Boolean
from ..db_setup import Base

class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(300), nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)