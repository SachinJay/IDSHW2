"""
Experiment with how security logs are printed
"""
from time import sleep
from utils import convert_windows_date
import win32evtlog


from constants import SECURITY, TIME_ATTR
from constants import EVENT_ATTRS


def filter_sec(attr, value):
    # Filters out useless info from StringInserts
    if attr == "StringInserts":
        try:
            value = value[6:8]
            file_str = value[0]
            hex = value[1]
            hex = int(str(hex))

            value = file_str,hex
        except:
            print(f"This value caused failure: {value}")

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
                for attr in EVENT_ATTRS:
                    value = getattr(event, attr)
                    value = filter_sec(attr, value)
                    print(value, end = " ")
                print()

    win32evtlog.CloseEventLog(hand)

def print_sec_every_min():
    while 1:
        print_sec()
        sleep(60)

def main():
    print_sec_every_min()

if __name__ == "__main__":
    main()
