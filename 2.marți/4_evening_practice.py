# 4_evening_practice.py

# EXERCIȚIU
# scrieți o funcție `def timer(minutes)`
# ce la fiecare secundă printează timpul rămas până la 0,
# în format "M:SS".

from time import sleep


def timer(mins):
    secs = mins * 60

    while secs > 0:
        m = secs // 60
        s = secs % 60

        print("%i:%02i" % (m, s))
        sleep(1)

        secs -= 1

# timer(1)


# EXERCIȚIU:
# alertă dacă este ora de pauză

# - să verificăm ceasul

import datetime

now = datetime.datetime.now()
alert_hour = datetime.time(11)

