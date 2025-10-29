
# EXERCIȚIU:
# alertă dacă este ora de pauză

# - să verificăm ceasul

from datetime import datetime, timedelta
from time import sleep
import subprocess


def runat(dt, payload):
    now = datetime.now()
    delta = dt - now
    seconds = delta.total_seconds()

    sleep(seconds)
    payload()


def timespec_to_dt(hour, minute, second):
    """
    returns a datetime object, at the given
    hour, minute, second, at their next ooccurence.
    
    that is, either today or tomorrow.
    """

    now = datetime.now()
    future = now.replace(hour=hour,
                         minute=minute,
                         second=second)
    
    if future < now:
        # we need to make it tomorrow
        future += timedelta(days=1)

    return future


def alarm(hour, minute, second):
    when = timespec_to_dt(hour, minute, second)

    def alert():
        subprocess.run([
            'notify-send',
            '-a', "Alarmă",
            "Este ora %s:%s:%s" % (hour, minute, second),
        ])

    runat(when, alert)
