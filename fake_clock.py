import time
import threading
class Clock:
    def get_current_time(self):
        raise NotImplementedError()

class SystemClock(Clock):
    def get_current_time(self):
        return time.time()

class FakeClock(Clock):
    def __init__(self, initial_time):
        self.current_time = initial_time

    def get_current_time(self):
        return self.current_time

    def set_current_time(self, new_time):
        self.current_time = new_time

class Scheduler:
    def __init__(self, clock):
        self.clock = clock

    def schedule_task(self, task, delay):
        current_time = self.clock.get_current_time()
        # scheduled_time = current_time + delay
        scheduled_time = current_time + delay
        # Perform scheduling logic here
        print(f"Time now is: {current_time}")
        print(f"Task scheduled for {scheduled_time}")
        def execute_task():
            print(f"Task: {task} is being executed now: {self.clock.get_current_time()}!")
                # Add your task execution logic here

        timer_thread = threading.Timer(delay, execute_task)
        timer_thread.start()
# Testing the scheduler with the fake clock implementation
fake_clock = FakeClock(initial_time=0)
scheduler = Scheduler(clock=fake_clock)

# Set the fake clock to a specific time
fake_clock.set_current_time(10)

# Schedule a task to run after 5 seconds
scheduler.schedule_task("Task A", 5)

# The task will be scheduled for 15 seconds (current time + delay)
print("Life continues while waiting for task...")