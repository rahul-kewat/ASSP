from Models import Song
from Config.database import engine, SessionLocal
from sqlalchemy.orm import Session

def get_song_by_id(db: Session, id: int):
    return db.query(Song.Song).filter(Song.Song.id == id).first()

def get_songs(db: Session):
    return db.query(Song.Song).all()

def delete_song_by_id(db: Session,id):
    db.query(Song.Song).filter(Song.Song.id == id).delete()
    db.commit()
    return 1

def save_song(db: Session,request):
    song = Song.Song(song_name=request.meta_data.name, duration=request.meta_data.duration)
    db.add(song)
    db.commit()
    db.refresh(song)
    return song

def update_song(db: Session,request,id):
    song = get_song_by_id(db,id)
    if song is None:
        return 0
    song.song_name = request.meta_data.name
    song.duration=request.meta_data.duration
    db.commit()
    db.refresh(song)
    return song