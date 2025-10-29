#!/usr/bin/env python

# EXERCIȚIU

# script stand-alone
# să primească timpul în format hh:mm:ss / mm:ss / ss

# scrieți o funcție `def timer(minutes)`
# ce la fiecare secundă printează timpul rămas până la 0,
# în format "M:SS".


import sys
from time import sleep


def fmt_seconds(secs):
    m = secs // 60
    s = secs % 60

    return "%i:%02i" % (m, s)

def timer(seconds):
    # calculate initial length, to keep
    # futher output aligned
    v = fmt_seconds(seconds)
    initial_len = len(v)

    while seconds > 0:
        v = fmt_seconds(seconds)
        # always keep the output aligned to initial length
        out = v.rjust(initial_len)

        sys.stdout.write(out)
        # flush forcibly, so the output isn't buffered
        sys.stdout.flush()

        sleep(1)
        seconds -= 1

        # backspace to line start
        sys.stdout.write("\b" * initial_len)
        # equivalent with
        #sys.stdout.write("\r")

    # finally:
    sys.stdout.write("0:00".rjust(initial_len))
    # also write an "enter"
    sys.stdout.write("\n")


# scriem o funcție care parsează input de forma
# "hh:mm:ss" / "mm:ss" / "ss"
# și returnează numărul de secunde

def time_to_seconds(v):
    """
    converts a string of the format 
          "ss"
       "mm:ss"
    "hh:mm:ss"
    into the number of seconds it represents
    """

    parts = v.split(":")

    # early exit if invalid input
    if len(parts) > 3:
        raise ValueError("Invalid time format: '%s'." % v)

    elif len(parts) == 1 and not parts[0]:
        raise ValueError("Function requires an argument.")

    try:
        parts = [int(elem) for elem in parts]
    except ValueError:
        raise ValueError("Invalid time format: '%s'." % v)

    """
    # we extract h, m, s. [*]

    # [*] v1: by repeated popping and eror handling.
    #
    # `h` and `m` may be missing,
    # `s` is never missing
    h, m = 0, 0

    try:
        s = parts.pop()
        m = parts.pop()
        h = parts.pop()
    except IndexError:
        pass
    """

    # [*] v2: if / elif / else. friendly version.

    if len(parts) == 3:
        h, m, s = parts

    elif len(parts) == 2:
        h = 0
        m, s = parts

    else:
        h, m = 0, 0
        s = parts[0]

    # [*] v3: using match. kinda pretty.

    match len(parts):
        case 3:
            h, m, s = parts
        case 2:
            h = 0
            m, s = parts 
        case 1:
            h, m = 0, 0
            s = parts[0]


    # [*] v3.x: still match, but going crazy.

    match len(parts):
        case 3:
            h, m, s = parts
        case 2:
            h, (m, s) = 0, parts 
        case 1:
            h, m, (s, ) = 0, 0, parts


    total_seconds = h*3600 + m*60 + s
    return total_seconds


# detectăm dacă suntem importați ca modul
# sau suntem executați direct.
if __name__ == '__main__':
    try:
        timespec = sys.argv[1]
    except IndexError:
        print("Usage: %s [[hh:]mm:]ss" % sys.argv[0], file=sys.stderr)
        sys.exit(1)

    try:
        seconds = time_to_seconds(timespec)
    except ValueError as e:
        msg = e.args[0]
        print(msg, file=sys.stderr)
        sys.exit(1)

    timer(seconds)


"""

There are 2 hard problems in computing:
- naming things,
- cache invalidation,
- off-by-one errors.


"""
