from database import SessionLocal
from models import Worker, Workstation, Event
from datetime import datetime, timedelta
import random


def seed_data():
    db = SessionLocal()
    db.query(Event).delete()
    db.query(Worker).delete()
    db.query(Workstation).delete()


    workers = [Worker(worker_id=f"W{i}", name=f"Worker {i}") for i in range(1,7)]
    stations = [Workstation(station_id=f"S{i}", name=f"Station {i}") for i in range(1,7)]


    db.add_all(workers + stations)


    now = datetime.utcnow()
    for _ in range(200):
        e = Event(
        timestamp=now - timedelta(minutes=random.randint(1,500)),
        worker_id=random.choice(workers).worker_id,
        workstation_id=random.choice(stations).station_id,
        event_type=random.choice(["working","idle","product_count"]),
        confidence=round(random.uniform(0.85,0.99),2),
        count=random.randint(1,5)
        )
        db.add(e)


    db.commit()
    db.close()