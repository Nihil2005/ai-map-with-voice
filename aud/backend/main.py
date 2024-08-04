from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)

@app.get("/locations/", response_model=list[schemas.Location])
def read_locations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations

@app.get("/locations/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location
