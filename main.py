from alarm_clock import AlarmClock

my_clock = AlarmClock()
print(f"The current time is {my_clock.current_time}")
my_clock.set_current_time("0358")
my_clock.alarm_clock_toggle()
my_clock.alarm_clock_toggle()