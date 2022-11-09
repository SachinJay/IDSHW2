LOGFILE = "log_types.txt"
DATA_FILE = "sensor.csv"

SYSTEM = "System"
SECURITY = "Security"
# EVENT_ATTRS = ["TimeGenerated", "EventType", "EventCategory", "StringInserts"]
EVENT_ATTRS = ["TimeGenerated", "StringInserts"]
SEC_ATTRS = ["TimeGenerated", "StringInserts"]
TIME_ATTR = "TimeGenerated"
STRING_ATRR = "StringInserts"

"""
These are paths we are not interested in. For whatever reason that may be,
mostly because they are used too often and are not interesting because
they are not files
"""
BLOCKED_PATHS = ["C:\\Users\\sachi\\OneDrive", 
"C:\\Users\\sachi\\OneDrive\\Desktop", 
"C:\\Users\\sachi\\OneDrive\\Desktop\\Microsoft Edge.lnk",
"C:\\Users\\sachi\\OneDrive\\Desktop\\MinGW Installer.lnk",
"C:\\Users\\sachi\\OneDrive\\desktop.ini",
"C:\\Users\\sachi\\OneDrive\\Desktop\\desktop.ini"]

BLOCKED_DIRS = ["\\.git", "\\G++", "\\commons-math", "\\openmrs-core",
 "\\Desktop\\hw-1", "\\Desktop\\TestOutput", "\\Desktop\\TestInput",
 "\\Desktop\\TestOutput", "\\Sorry to Bother You"]