import threading
import pygame

# By Gudni Natan Gunnarsson, 2017

class Timer(object):
    def __init__(self, event, rate):
        self.running = False
        self.event = event
        self.rate = rate
        self.t = threading.Thread(target=self.eventPoster, args=(event, rate))
        self.t.daemon = True
        self.ok = threading.Event()

    def go(self):
        self.ok.set()

    def eventPoster(self, event, rate):
        e = pygame.event
        go = self.go

        def wait(rate):
            self.ok.clear()
            goThread = threading.Timer(float(rate) / 1000.0, go)
            goThread.daemon = True
            goThread.start()
            self.ok.wait()
            if goThread.is_alive() and self.running:
                goThread.join()

        wait(rate)
        while self.running:
            if type(event) is e.EventType:
                e.post(event)
            else:
                e.post(e.Event(event))
            wait(rate)

    def start_timer(self):
        self.running = True
        self.t.start()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.ok.set()
            self.t.join()

    def change_rate(self, rate):
        self.rate = rate

class BetterTimers(object):
    def __init__(self):
        self.timers = list()

    def set_timer(self, event, rate):
        t = Timer(event, rate)
        for e in self.timers:
            if e.event == event:
                if rate > 0:
                    e.change_rate(rate)
                else:
                    e.stop_timer()
                    self.timers.remove(e)
                return
        if rate > 0:
            t.start_timer()
            self.timers.append(t)

    def end_all_timers(self):
        for t in self.timers:
            t.stop_timer()

        self.timers = list()
