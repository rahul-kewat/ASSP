from pydantic import (BaseModel,conint, ValidationError, validator, constr, conlist)
from typing import List, Optional, Set

class GenericRequest(BaseModel):
    name:constr(max_length=100,min_length=1)
    duration:conint(gt=0)
    author:constr(max_length=100)
    host:constr(max_length=100)
    narrator:constr(max_length=100)
    duration:conint(gt=0) 
    participants: conlist(str,max_items= 10 , min_items=0)

class SongRequest(BaseModel):
    song_name:constr(max_length=100)
    duration:conint(gt=0)

class PodcastRequest(BaseModel):
    podcast_name:constr(max_length=100)
    duration:conint(gt=0) 
    host:constr(max_length=100)
    participants: conlist(str, max_items= 10 , min_items=0)

class AudiobookRequest(BaseModel):
    podcast_name:constr(max_length=100)
    author_name:constr(max_length=100)
    narrator:constr(max_length=100)
    duration:conint(gt=0)     

class AudioRequest(BaseModel):
    file_type:conint(gt=0, lt=4)
    meta_data:GenericRequest

class UpdateAudioRequest(BaseModel):
    meta_data:GenericRequest

