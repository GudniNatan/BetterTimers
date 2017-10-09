from threading import Thread, Timer as threadTimer
from pygame import event as pyEvent
from math import floor

# By Gudni Natan Gunnarsson, 2017

class Timer(object):
    def __init__(self, event, rate):
        self.running = False
        self.event = event
        self.rate = rate
        self.t = Thread(target=self.eventPoster, args=(event, rate))
        self.t.daemon = True

    def eventPoster(self, event, rate):
        e = pyEvent
        def post(event, rate):
            if self.running:
                if type(event) is e.EventType:
                    e.post(event)
                else:
                    e.post(e.Event(event))
                goThread.run()

        goThread = threadTimer(float(rate - 1) / 1000.0, post, args=(event, rate,))
        goThread.daemon = True
        goThread.start()

    def start_timer(self):
        self.running = True
        self.t.start()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.t.join()

    def change_rate(self, rate):
        self.rate = rate

class BetterTimers():
    def __init__(self):
        self.timers = list()

    def delayedEventHandling(self, event, rate):
        self.set_timer(event, rate)


    def set_timer(self, event, rate, delay=0):
        if floor(delay) > 0:
            delayTimer = threadTimer(delay-1, self.delayedEventHandling, args=(event, rate,))
            delayTimer.daemon = True
            delayTimer.start()
            return

        t = Timer(event, rate)
        for e in self.timers:
            if e.event == event:
                if floor(rate) > 0:
                    e.change_rate(rate)
                else:
                    e.stop_timer()
                    self.timers.remove(e)
                return
        if floor(rate) > 0:
            t.start_timer()
            self.timers.append(t)

    def end_all_timers(self):
        for t in self.timers:
            t.stop_timer()

        self.timers = list()

timers = BetterTimers()
