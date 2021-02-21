from typing import List

from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from Config.database import SessionLocal, engine
from Service import DataService
from Requests import AudioRequest

from Requests import AudioRequest
router_audio = APIRouter(
    prefix="/audio",
    tags=["audio"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router_audio.post("/save", summary="Save audio based upon audio type", description="Save the audio")
def save_audio(request: AudioRequest.AudioRequest , db: Session = Depends(get_db)):
    return DataService.save_audio(db,request)

@router_audio.delete("/{audio_type}/{id}", summary="Delete audio by ID", description="delete audio details")
def delete_audio_by_id(audio_type:int,id:int,db: Session = Depends(get_db)):
    if (audio_type not in [1,2,3]  ):
        raise HTTPException(status_code=422, detail="Invalid Audio Type")
    status = DataService.delete_data_by_type_and_id(db,audio_type,id)
    if status == 0:
        raise HTTPException(status_code=404, detail="Audio not found")
    return {"message" : "Deleted Successfully"}

@router_audio.patch("/{audio_type}/{id}", summary="Update audio based upon audio type", description="Update the audio")
def update_audio(audio_type:int,id:int,request: AudioRequest.UpdateAudioRequest , db: Session = Depends(get_db)):
    if (audio_type not in [1,2,3]  ):
        raise HTTPException(status_code=422, detail="Invalid Audio Type")
    status = DataService.update_audio(db,request,audio_type,id)
    if status == 0 :
        raise HTTPException(status_code=404, detail="Audio not found")
    return status

@router_audio.get("/{audio_type}/{id}", summary="Get audio by ID", description="Returns audio details")
def get_audio_by_id(audio_type:int ,id:int,db: Session = Depends(get_db)):
    if (audio_type not in [1,2,3]  ):
        raise HTTPException(status_code=422, detail="Invalid Audio Type")
    data = DataService.get_data_by_type_and_id(db,audio_type,id)
    if not data:
        raise HTTPException(status_code=404, detail="Audio not found")
    return data 

@router_audio.get("/", summary="Get all audio from the server", description="Returns all the audio category wise")
def get_audio( db: Session = Depends(get_db)):
    return DataService.get_all_audio(db)
