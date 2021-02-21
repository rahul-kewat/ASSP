from Models import Podcast
from Models import PodcastParticipants
from Config.database import engine, SessionLocal
from sqlalchemy.orm import Session

def get_podcast_by_id(db: Session, id: int):
    podcast = db.query(Podcast.Podcast).filter(Podcast.Podcast.id == id).first()
    if podcast is not None:
        podcastParticipants = db.query(PodcastParticipants.PodcastParticipants).filter(PodcastParticipants.PodcastParticipants.podcast_id == id).all()
        podcast.participant = podcastParticipants 
    return podcast

def get_podcasts(db: Session):
    allpodcasts = db.query(Podcast.Podcast).all()
    length = len(allpodcasts)
    for i in range(length):
        podcastParticipants = db.query(PodcastParticipants.PodcastParticipants).filter(PodcastParticipants.PodcastParticipants.podcast_id == allpodcasts[i].id).all()
        allpodcasts[i].participant = podcastParticipants 
    return allpodcasts

def delete_podcast_by_id(db: Session,id):
    db.query(Podcast.Podcast).filter(Podcast.Podcast.id == id).delete()
    db.query(PodcastParticipants.PodcastParticipants).filter(PodcastParticipants.PodcastParticipants.podcast_id == id).delete()
    db.commit()
    return 1

def save_podcast(db: Session,request):
    podcast = Podcast.Podcast(podcast_name=request.meta_data.name, duration=request.meta_data.duration, host=request.meta_data.host)
    db.add(podcast)
    db.commit()
    db.refresh(podcast)
    for parti in request.meta_data.participants:
        participant = PodcastParticipants.PodcastParticipants(podcast_id = podcast.id ,participant_name = parti)
        db.add(participant)
        db.commit()

    return get_podcast_by_id(db,podcast.id)

def update_podcast(db: Session,request,id):
    podcast = get_podcast_by_id(db,id)
    if podcast is None:
        return 0
    podcast.podcast_name=request.meta_data.name
    podcast.duration=request.meta_data.duration
    podcast.host=request.meta_data.host
    db.query(PodcastParticipants.PodcastParticipants).filter(PodcastParticipants.PodcastParticipants.podcast_id == id).delete()
    for parti in request.meta_data.participants:
        participant = PodcastParticipants.PodcastParticipants(podcast_id = podcast.id ,participant_name = parti)
        db.add(participant)
        db.commit()
    db.commit()
    db.refresh(podcast)
    return podcast