# BetterTimers
Better timers for pygame with demo


For in-depth explanation (in Icelandic) see:
https://gudninathan.blogspot.is/2017/05/pygame-og-events-1-genericevent.html


## Quick start

Start by downloading the package!
```
$ pip install pygame
$ pip install better_timers-gudninatan
```


Import timer manager
```
from better_timers import timers
```

__OR__

Create a new timer manager
```
from better_timers import BetterTimers
timers = BetterTimers()
```

Add new timers that will automatically go to the event queue repeatedly, every N milliseconds using this format.  
`timers.set_timer(event, ms, *delay_ms)`  
You can pass in both the regular USEREVENT types or create your own `pygame.event.Event` with any custom args and kwargs for unlimited possibilities. Override already established timers easily, or delete them entirely by passing in a rate of 0 or less.

```
genericEvent = USEREVENT + 1
randomEvent = USEREVENT + 2

coolEvent = pygame.event.Event(genericEvent, code="cool")
uncoolEvent = pygame.event.Event(genericEvent, code="uncool")

timers.set_timer(coolEvent, 500) # Sets a timer for 500 milliseconds
timers.set_timer(coolEvent, 2000, 300) # Overrides old 500 rate timer, with delay

timers.set_timer(uncoolEvent, 1000) # New genericEvent timer with a different code

timers.set_timer(randomEvent, 5000) # Traditional timer set with USEREVENT
timers.set_timer(randomEvent, 0) # Timer stopped
```

You will recieve these events in the pygame event queue just as you would expect.

	while True:
	    ...
	    for event in pygame.event.get():
	        ...
	        if event == coolEvent:
	            print("How cool!")
	    ...

All timers will be stopped upon calling `pygame.quit()`. You can also stop all the timers with this neat shortcut:

	timers.end_all_timers()
	

## Compatability

better_timers is compatible with both python 2 & 3.

## Dependencies

better_timers is dependant on [pygame](http://www.pygame.org).
