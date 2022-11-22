# Intro

For this project, I worked on a Windows laptop and as such I used the
`sensor.py` starter code provided. I built off of this starter code and my
resulting code can be found [here](https://github.com/SachinJay/IDSHW2)

The big picture idea I had was to try and pare down the amount of data gathered
as much as possible. I didn't want to have too many features from too many audit
sources creating too much data. I did not want this because there could be
spurious correlations picked up by the model that led to a bad predictor of
normal behavior. That is to say, my approach was to try and use only the most
important features and audit sources based on my knowledge of how I use my
computer.

# Audit Sources

As instructed in the `project2.pdf`, I enabled auditing on the File System. I
then pared down `input.txt` based on knowledge of how I used my computer and
test runs of my sensor.

Test runs of my sensor revealed too much data being collected. I ran the sensor
for one minute and calculated that based on the amount of data that was
collected in that minute, an hour of collecting data would amass 6GB of data.
This was obviously not feasible to gather over 4 days so I trimmed `input.txt`
down until there was just one line left: `C:\Users`

I know that this is where I do almost all of my interation with my computer's
filesystem and so I figured this would be representative of my usage profile.

To recap: my sole audit source was the File System of my computer, specifically
the `C:\Users` directory. I narrowed it down to this in order to have a
representative and compact dataset.

# Features

I did a lot of experimenting before settling on the features I would finally
use.

First, I experimented with the different log types. The Windows Event Log has
581 log types that I could discover. I used the code in `logtypes.py` (see
references) in order to discover this. I experimented with some of the log types
that seemed most interesting to me, specifically **System** and **Application**
as well as the default **Security** given to us.

I tried determing which one is best by reading the documentation, but Microsoft's
documentation on the area was sparse at best. So instead of that, I created the
script `do.py` to simulate my usage of the machine and then I checked which
log type actually picked up on these changes.

`do.py` creates, writes to, waits, and then deletes 3 different .txt files. The
only log type that picked up on these changes was the **Security** logs and so
I used those.

After settling on using the **Security** logs, I experimented with what features
to use to train my model. Looking at all the information captures in the
different event attributes, I noticed that the Event Category and Event Type
attributes were all the same for the Security events and so I discarded these.

Furthermore, I noticed that much of the String Inserts attribute seemed like
unexplained codes and so I disregarded most of these in case it caused too much
noise. I kept one such field as my last feature, just in case it was
discriminative.

I know that the time I use my computer is a very discriminative feature since
I only really use it within certain regular hours. So I kept the TimeGenerated
event attribute and made converted it into two numbers. See the references for
the resouce I used to do this. I broke the TimeGenerated attribute up into the
day an event was generated and the hour.

The last feature to talk about is the third of my four features: the file
that was touched. I extracted the name of the file from the StringInserts field
and kept this as a feature. I had some reservations about this because I was not
sure how well a model would respond to a string. But in the end I knew that I
needed to capture what files were touched in my model in order to properly
discriminate if a user was me or not so I included this feature.

# Code

The functions in my code have detailed docstrings, however the organization
needs some explaining.

`sensor.py` contains mostly vestigial code from my initial testing. In its main
method it calls code from `sec.py` which is where most of my implementation
actually resides. This structures is a vestige of how I initially did some
testing in `sensor.py` but then moved my testing of the **Security** logs to
`sec.py`.

# Model

# Team Work

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
- [Python datetime object](https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime)
    - for converting datetime in the logs to usable features
