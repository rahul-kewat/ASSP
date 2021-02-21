from sqlalchemy import Column, Integer, String, DateTime
from Config.database import Base
from Models import Podcast

class PodcastParticipants(Base):
    __tablename__ = "podcast_participant"

    id = Column(Integer, primary_key=True, index=True)
    podcast_id = Column(Integer)
    participant_name = Column(String(100))
