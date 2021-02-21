import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from Routes import routes
from Config import database
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Models import Audiobook

from Config import database

app = FastAPI(title="ASSP", description="Audio Server Simulation Program")


app.include_router(routes.router_audio)

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)