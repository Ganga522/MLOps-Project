from database import SessionLocal
from models import Event
from collections import defaultdict


def compute_metrics():
    db = SessionLocal()
    events = db.query(Event).all()


    workers = defaultdict(lambda: {"active":0,"idle":0,"units":0})
    stations = defaultdict(lambda: {"occupancy":0,"units":0})


    for e in events:
        if e.event_type == "working": workers[e.worker_id]["active"] += 1
        if e.event_type == "idle": workers[e.worker_id]["idle"] += 1
        if e.event_type == "product_count":
            workers[e.worker_id]["units"] += e.count
            stations[e.workstation_id]["units"] += e.count
            stations[e.workstation_id]["occupancy"] += 1


    factory = {
    "total_productive_time": sum(w["active"] for w in workers.values()),
    "total_production": sum(w["units"] for w in workers.values()),
    "average_utilization": round(sum(w["active"]/(w["active"]+w["idle"]+1) for w in workers.values())/6,2)
    }


    return workers, stations, factory