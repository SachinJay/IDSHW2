import win32evtlog
import sys

ERROR_MSG = """Usage:
\nsensor.py s to print a snapshot
\nsensor.py c to print continuously
\nsensor.py defualts to print a snapshot\n"""


def print_snapshot():
    hand = win32evtlog.OpenEventLog("localhost", "Security")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    events = win32evtlog.ReadEventLog(hand, flags, 0)

    # To ensure the data generated is all of the same shape
    # print(dir(events[0]))

    for event in events:
        print(event.TimeGenerated, event.EventType, event.EventCategory, event.Data, event.StringInserts)
        # break

def continuously_print_events():
    while(1):
        print_snapshot()

def print_error_msg():
    print(ERROR_MSG)


def driver():

    if len(sys.argv) == 1:
        print_snapshot()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'c':
            continuously_print_events()
        elif sys.argv[1] == 's':
            print_snapshot()
        else:
            print_error_msg()
            exit(1)


    


if __name__ == "__main__":
    driver()
    