from sqlalchemy import Column, Integer, String, DateTime
from Config.database import Base
from Models import PodcastParticipants
from typing import List
import datetime

class Podcast(Base):
    __tablename__ = "podcast"

    id = Column(Integer, primary_key=True, index=True)
    podcast_name = Column(String(100))
    duration = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    host = Column(String(100))
    participants = PodcastParticipants


