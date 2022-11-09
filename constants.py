LOGFILE = "log_types.txt"

SYSTEM = "System"
SECURITY = "Security"
# EVENT_ATTRS = ["TimeGenerated", "EventType", "EventCategory", "StringInserts"]
EVENT_ATTRS = ["TimeGenerated", "StringInserts"]
SEC_ATTRS = ["TimeGenerated", "StringInserts"]
TIME_ATTR = "TimeGenerated"
STRING_ATRR = "StringInserts"

BLOCKED_PATHS = ["C:\\Users\\sachi\\OneDrive", "C:\\Users\\sachi\\OneDrive\\Desktop"]
BLOCKED_DIRS = ["\\.git", "\\G++", "\\commons-math", "\\openmrs-core",
 "\\Desktop\\hw-1"]