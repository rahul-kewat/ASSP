from sqlalchemy import Column, Integer, String, DateTime
from Config.database import Base
import datetime

class Audiobook(Base):
    __tablename__ = "audiobook"

    id = Column(Integer, primary_key=True, index=True)
    audiobook_name = Column(String(100))
    author = Column(String(100))
    narrator = Column(String(100))
    duration = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    
