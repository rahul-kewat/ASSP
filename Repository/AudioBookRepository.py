from Models import Audiobook
from Config.database import engine, SessionLocal
from sqlalchemy.orm import Session

def get_audiobook_by_id(db: Session, id: int):
    return db.query(Audiobook.Audiobook).filter(Audiobook.Audiobook.id == id).first()

def get_audiobooks(db: Session):
    return db.query(Audiobook.Audiobook).all()

def delete_audiobook_by_id(db: Session,id):
    db.query(Audiobook.Audiobook).filter(Audiobook.Audiobook.id == id).delete()
    db.commit()
    return 1

def save_audiobook(db: Session,request):
    audiobook = Audiobook.Audiobook(audiobook_name=request.meta_data.name, author=request.meta_data.author, narrator= request.meta_data.narrator, duration=request.meta_data.duration)
    db.add(audiobook)
    db.commit()
    db.refresh(audiobook)
    return audiobook

def update_audiobook(db: Session,request,id):
    audiobook = get_audiobook_by_id(db,id)
    if audiobook is None:
        return 0
    audiobook.audiobook_name=request.meta_data.name
    audiobook.author=request.meta_data.author
    audiobook.narrator= request.meta_data.narrator
    audiobook.duration=request.meta_data.durationn
    db.commit()
    db.refresh(audiobook)
    return audiobook