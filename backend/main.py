from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ ADD
from database import Base, engine, SessionLocal
from models import Event
from schemas import EventSchema
from seed import seed_data
from metrics import compute_metrics

app = FastAPI()

# ✅ ADD CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
seed_data()

@app.post("/events")
def ingest_event(event: EventSchema):
    db = SessionLocal()
    e = Event(**event.dict())
    db.add(e)
    db.commit()
    return {"status":"stored"}

@app.get("/metrics/workers")
def worker_metrics():
    workers,_,_ = compute_metrics()
    return workers

@app.get("/metrics/workstations")
def workstation_metrics():
    _,stations,_ = compute_metrics()
    return stations

@app.get("/metrics/factory")
def factory_metrics():
    _,_,factory = compute_metrics()
    return factory

@app.post("/seed")
def reseed():
    seed_data()
    return {"status":"reseeded"}
