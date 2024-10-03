# main.py
from fastapi import FastAPI
from users.controller import router
import users.models as models
from database.database import engine

app = FastAPI()

# Include the router from the controller
app.include_router(router)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=engine)
