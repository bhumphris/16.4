class Time:
    def __init__(self):
        self.minute = None
        self.second = None
        self.hour = None

def time_to_int(time):
    minute = time.hour * 60 + time.minute
    seconds = minute * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(time, inc):
    time1 = time
    time1 += inc
    return time1

time = Time()
time.hour = 12
time.minute = 59
time.second = 55

print ('\nThe time to be incremented is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

time.seconds = time_to_int(time)

inc_sec = raw_input('\nEnter the number of seconds to incremen the time object by: ')

print ('\nThe amount time will be incremented by is: ' + str(inc_sec) + ' seconds. ')
inc_seconds = increment(time.seconds, int(inc_sec))

time1 = int_to_time(inc_seconds)

if time1.hour > 12:
    time1.hour -= 12

print ('\nThe original time was ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
print ('\nThe incremented time is ' + '%.2d:%.2d:%.2d' % (time1.hour, time1.minute, time1.second))
