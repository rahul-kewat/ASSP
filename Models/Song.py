from sqlalchemy import Column, Integer, String, DateTime
from Config.database import Base
import datetime

class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True, index=True)
    song_name = Column(String(100))
    duration = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)

