from typing import List
from typing import Dict
from sqlalchemy.orm import Session
from Repository import AudioBookRepository
from Repository import PodcastRepository
from Repository import SongRepository
from Config.database import engine, SessionLocal
from Models import Audiobook
from Models import Podcast
from Models import PodcastParticipants
from Models import Song
from fastapi import APIRouter, HTTPException, Response, Request

Audiobook.Base.metadata.create_all(bind=engine)
Podcast.Base.metadata.create_all(bind=engine)
PodcastParticipants.Base.metadata.create_all(bind=engine)
Song.Base.metadata.create_all(bind=engine)

def get_all_audio(db :Session):
    audiobookdata = AudioBookRepository.get_audiobooks(db)
    podcastdata = PodcastRepository.get_podcasts(db)
    songdata = SongRepository.get_songs(db)
    return {"audiobook": audiobookdata, "podcasts": podcastdata, "songs":songdata}

def get_data_by_type_and_id(db,audio_type:int , id:int):
    if(audio_type == 3):
        return AudioBookRepository.get_audiobook_by_id(db,id)
    if(audio_type == 2):
        return PodcastRepository.get_podcast_by_id(db,id)
    if(audio_type == 1):
        return SongRepository.get_song_by_id(db,id)

def delete_data_by_type_and_id(db, audio_type:int, id:int):
    if(audio_type == 3):
        if AudioBookRepository.get_audiobook_by_id(db,id) is None :
            return 0
        return AudioBookRepository.delete_audiobook_by_id(db,id)
    if(audio_type == 2):
        if PodcastRepository.get_podcast_by_id(db,id)  is None:
            return 0
        return PodcastRepository.delete_podcast_by_id(db,id)
    if(audio_type == 1):
        if SongRepository.get_song_by_id(db,id) is None:
            return 0
        return SongRepository.delete_song_by_id(db,id)

def save_audio(db,request):
    if(request.file_type == 3):
        if not request.meta_data.author.strip() or not request.meta_data.narrator.strip():
            raise HTTPException(status_code=422, detail="Please pass valid data")
        status = AudioBookRepository.save_audiobook(db,request)
    if(request.file_type == 2):
        if not request.meta_data.host.strip():
            raise HTTPException(status_code=422, detail="Please pass valid data")
        for participant in request.meta_data.participants:
            if not participant:
                raise HTTPException(status_code=422, detail="Please pass valid data")
        status = PodcastRepository.save_podcast(db,request)
    if(request.file_type == 1):
        status = SongRepository.save_song(db,request)
    return status
    
def update_audio(db,request,audio_type,id):
    if(audio_type == 3):
        if not request.meta_data.author.strip() or not request.meta_data.narrator.strip():
            raise HTTPException(status_code=422, detail="Please pass valid data")
        status = AudioBookRepository.update_audiobook(db,request,id)
    if(audio_type == 2):
        if not request.meta_data.host.strip():
            raise HTTPException(status_code=422, detail="Please pass valid data")
        for participant in request.meta_data.participants:
            if not participant:
                raise HTTPException(status_code=422, detail="Please pass valid data")
        status = PodcastRepository.update_podcast(db,request,id)
    if(audio_type == 1):
        status = SongRepository.update_song(db,request,id)
    return status
    