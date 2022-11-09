"""
Experiment with how security logs are printed
"""
from time import sleep
from utils import convert_windows_date
import win32evtlog
import csv


from constants import BLOCKED_DIRS, BLOCKED_PATHS, DATA_FILE, SECURITY, STRING_ATRR, TIME_ATTR
from constants import EVENT_ATTRS


def is_bad_path(path : str) -> bool:
    """
    Returns true if this path makes the event skippable
    """    

    if path in BLOCKED_PATHS:
        return True

    for dir in BLOCKED_DIRS:
        if dir in path:
            return True

    if "C:\\Users\\sachi\\OneDrive" not in path:
        return True

    return False


def can_skip_event(event) -> bool:
    """
    Checks if we can skip an event
    We can skip an event for a number of reasons
        - If the event is common: e.g. most file touches will happen in the 
        C:\\Users directory so events regarding only that dir aren't interesting
        - If the event is irrelevant: e.g. events not trigerred by a human
        aren't very interesting. I'm not sure if I should wholesale disregard
        them though?
    """
    value = getattr(event, STRING_ATRR)

    try:
        path = value[6]
        if is_bad_path(path):
            return True
    except Exception as e:
        print(f"Value {value} caused {e}")

    return False


def clean_sec_value(attr, value):
    # Filters out useless info from StringInserts
    if attr == "StringInserts":
        try:
            value = value[6:8]
            file_str = value[0]
            hex = value[1]
            hex = int(str(hex), base=16)

            value = file_str,hex
        except Exception as e:
            print(f"This value caused failure: {value} with error {e}")
            return None

    if attr == TIME_ATTR:
        value = convert_windows_date(str(value))

    return value

def print_sec():
    print(f"Printing security logs in the last minue only I think")

    hand = win32evtlog.OpenEventLog("localhost", SECURITY)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
   

    while 1:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        if events:
            for event in events:

                if can_skip_event(event):
                    # If we can skip this event, go to the next event
                    continue

                row = []
                event_parsed = True

                for attr in EVENT_ATTRS:

                    value = getattr(event, attr)
                    value = clean_sec_value(attr, value)
                    event_parsed = value is not None
                    if isinstance(value, tuple):
                        for element in value:
                            row.append(element)
                    else:
                        row.append(value)
                if event_parsed:
                    print(row)

    win32evtlog.CloseEventLog(hand)

def write_sec():
    print(f"writing security logs in the last minue only I think, to csv")

    csv_file = open(DATA_FILE, 'a', newline='')
    writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    print(f"Printing security logs in the last minue only I think")

    hand = win32evtlog.OpenEventLog("localhost", SECURITY)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
   

    while 1:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        if events:
            for event in events:

                if can_skip_event(event):
                    # If we can skip this event, go to the next event
                    continue

                row = []
                event_parsed = True

                for attr in EVENT_ATTRS:

                    value = getattr(event, attr)
                    value = clean_sec_value(attr, value)
                    event_parsed = value is not None
                    if isinstance(value, tuple):
                        for element in value:
                            row.append(element)
                    else:
                        row.append(value)
                if event_parsed:
                    writer.writerow(row)

    win32evtlog.CloseEventLog(hand)
    csv_file.close()

def every_min(func):
    while 1:
        func()
        sleep(60)



def main():
    every_min(write_sec)

if __name__ == "__main__":
    main()
