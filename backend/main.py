from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from models import Event
from schemas import EventSchema
from seed import seed_data
from metrics import compute_metrics
from datetime import datetime  # ✅ For proper timestamp

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables and seed initial data
Base.metadata.create_all(bind=engine)
seed_data()

@app.post("/events")
def ingest_event(event: EventSchema):
    db = SessionLocal()
    
    # Ensure timestamp is a datetime object
    event_data = event.dict()
    
    # If timestamp is optional or missing, set current datetime
    if "timestamp" not in event_data or not event_data["timestamp"]:
        event_data["timestamp"] = datetime.utcnow()
    else:
        # Convert string to datetime if necessary
        if isinstance(event_data["timestamp"], str):
            event_data["timestamp"] = datetime.fromisoformat(event_data["timestamp"])
    
    e = Event(**event_data)
    db.add(e)
    db.commit()
    db.refresh(e)  # ✅ Optional: get the inserted record back
    db.close()
    
    return {"status": "stored", "id": e.id, "timestamp": e.timestamp}

@app.get("/metrics/workers")
def worker_metrics():
    workers, _, _ = compute_metrics()
    return workers

@app.get("/metrics/workstations")
def workstation_metrics():
    _, stations, _ = compute_metrics()
    return stations

@app.get("/metrics/factory")
def factory_metrics():
    _, _, factory = compute_metrics()
    return factory

@app.post("/seed")
def reseed():
    seed_data()
    return {"status": "reseeded"}
