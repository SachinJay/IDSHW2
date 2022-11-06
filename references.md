# References

The following are some of the site I used to develop `sensor.py`

- [Stack overflow 1](https://stackoverflow.com/questions/61003020/python-2-7-pywin32-readeventlog-returns-partial-list-of-events)
    - I used this to read the entire contents of the log
- [Stack overflow 2](https://stackoverflow.com/questions/42944791/reading-windows-event-log-using-win32evtlog-module)
    - I used this to figure out how to continuously read from the buffer
    - It also helped me realize there are many different log types
- [Learning win32evtlog in python](https://stackoverflow.com/questions/42944791/reading-windows-event-log-using-win32evtlog-module)
    - This showed me how to get all possible log types. I used it to implement
    the main functionality of `logtypes.py`