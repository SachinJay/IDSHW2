import win32evtlog
import sys

from constants import SECURITY
from constants import SYSTEM
from constants import EVENT_ATTRS

from sec import write_sec
from sec import every_min

ERROR_MSG = """Usage:
\nsensor.py s to print a snapshot
\nsensor.py c to print continuously
\nsensor.py defualts to print a snapshot\n"""


def continuously_log_events(logtype=SECURITY):
    pass

def continuously_print_events(logtype=SECURITY):

    print(f"Log type is {logtype}")

    hand = win32evtlog.OpenEventLog("localhost", logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    num = 0

    while 1:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        if events:
            for event in events:
                for attr in EVENT_ATTRS:
                    print(getattr(event, attr), end = " ")
                # After we print out one line, create a new line for the next event
                print()
        # num = num + len(events)

    win32evtlog.CloseEventLog(hand)
    # print(num)

    # To ensure the data generated is all of the same shape
    # print(dir(events[0]))

    for event in events:
        for attr in EVENT_ATTRS:
            print(getattr(event, attr), end = " ")
        # After we print out one line, create a new line for the next event
        print()
    
    # after we have printed all events, print a new line
    print()

def print_snapshot():
    hand = win32evtlog.OpenEventLog("localhost", "Security")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    events = win32evtlog.ReadEventLog(hand, flags, 0)

    # To ensure the data generated is all of the same shape
    # print(dir(events[0]))

    for event in events:
        for attr in EVENT_ATTRS:
            print(getattr(event, attr), end = " ")
        # After we print out one line, create a new line for the next event
        print()
    
    # after we have printed all events, print a new line
    print()

        # print(event.TimeGenerated, event.EventType, event.EventCategory, event.Data, event.StringInserts)
        # break

def print_error_msg():
    print(ERROR_MSG)


def driver_old():

    print(EVENT_ATTRS)

    if len(sys.argv) == 1:
        continuously_print_events()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'c':
            continuously_print_events()
        elif sys.argv[1] == 's':
            print_snapshot()
        else:
            print_error_msg()
            exit(1)

def driver():
    # see sec.py for more details
    every_min(write_sec)


    


if __name__ == "__main__":
    driver()
    