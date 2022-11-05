import win32evtlog

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


if __name__ == "__main__":
    continuously_print_events()