import win32evtlog # requires pywin32 pre-installed
import csv

file = open('securityLogs.csv', 'w')
writer = csv.writer(file)
server = 'localhost' # name of the target computer to get event logs
logtype = 'Security' # 'Application' # 'Security'
hand = win32evtlog.OpenEventLog(server,logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

extractedEvents = [4608, 4609, 4648, 4624, 4625, 4634, 4649, 4657, 4660, 4661, 4662, 4664, 4665, 4666, 4667, 4668, 4670, 4688, 4689, 4691, 4697, 4698, 4699, 4700, 4701, 4702, 4703, 4704, 4705, 4706, 4707, 4709, 4710, 4717, 4718, 4719, 4720, 4722, 4723, 4724, 4725, 4726, 4727, 4782, 4873, 4880, 4881, 4945, 4946, 4947, 4948, 4949, 4950]
while True:
    events = win32evtlog.ReadEventLog(hand, flags,0)
    if events:
        for event in events:
                if event.EventID in extractedEvents:
                        print ('Event Category: ', event.EventCategory)
                        print ('Time Generated: ', event.TimeGenerated)
                        print ('Source Name: ', event.SourceName)
                        print ('Event ID: ', event.EventID)
                        print ('Event Type: ', event.EventType)
                        data = event.StringInserts
                        if data:
                                print (' Event Data: ')
                                for msg in data:
                                        print (msg)
                        writer.writerow([event.EventCategory,
                                                        event.TimeGenerated, event.SourceName,
                                                        event.EventID, event.EventType, data[0], 
                                                        data[1], data[2], data[3], data[4], data[5],
                                                        data[6]])  

                        print                            
file.close()