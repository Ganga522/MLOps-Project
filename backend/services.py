import hashlib

def event_hash(event):
    key = f"{event['timestamp']}{event['worker_id']}{event['workstation_id']}{event['event_type']}"
    return hashlib.md5(key.encode()).hexdigest()

