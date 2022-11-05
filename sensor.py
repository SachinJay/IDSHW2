import win32evtlog
import sys

LOGT1 = "System"
LOGT1 = "Security"


ERROR_MSG = """Usage:
\nsensor.py s to print a snapshot
\nsensor.py c to print continuously
\nsensor.py defualts to print a snapshot\n"""

EVENT_ATTRS = ["TimeGenerated", "EventType", "EventCategory", "Data", "StringInserts", "SourceName"]


def log_types():
    h = win32evtlog.EvtOpenChannelEnum(None)

    while win32evtlog.EvtNextChannelPath(h) is not None:
        
        print(win32evtlog.EvtNextChannelPath(h))


def con2():

    logtype = "Application"
    hand = win32evtlog.OpenEventLog("localhost", "System")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    num = 0

    while 1:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
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

def continuously_print_events():
    while(1):
        print_snapshot()

def print_error_msg():
    print(ERROR_MSG)


def driver():

    print(EVENT_ATTRS)

    if len(sys.argv) == 1:
        print_snapshot()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'c':
            con2()
        elif sys.argv[1] == 's':
            print_snapshot()
        else:
            print_error_msg()
            exit(1)


    


if __name__ == "__main__":
    driver()
    