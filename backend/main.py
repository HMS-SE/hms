from fastapi import FastAPI

from database import Base, engine
from database.models import *
from routes import users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)


@app.get("/__status__")
def status():
    return {"status": "OK"}
