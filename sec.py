"""
Experiment with how security logs are printed
"""
import win32evtlog


from constants import SECURITY
from constants import EVENT_ATTRS

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
                    print(getattr(event, attr), end = " ")
                print()

    win32evtlog.CloseEventLog(hand)

def print_sec_every_min():
    while 1:
        print_sec()

def main():
    print_sec_every_min()

if __name__ == "__main__":
    main()
