from datetime import datetime

def sort_events(events):
    return sorted(events, key=lambda x: x.timestamp)