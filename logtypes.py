"""
Records all the log types
"""

import win32evtlog
from constants import LOGFILE

def log_types():
    h = win32evtlog.EvtOpenChannelEnum(None)

    file = open(LOGFILE, 'w')

    print(f"Writing to {LOGFILE}")

    while win32evtlog.EvtNextChannelPath(h) is not None:
        logtype = win32evtlog.EvtNextChannelPath(h)
        if logtype:

            file.write(logtype)
            file.write("\n")

    print("Done!")
    file.close()


if __name__ == "__main__":
    log_types()
