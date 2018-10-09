from datetime import datetime, timedelta
import time

__all__ = ['get_datetime']


def get_datetime(utc0_time, delta=0):
    d = datetime.fromtimestamp(utc0_time) + timedelta(seconds=int(delta))
    utc8 = datetime.fromtimestamp(time.mktime(d.timetuple()))
    return utc8
