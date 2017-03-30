import pygame
from pygame.locals import *
from BetterTimers import BetterTimers
import sys
import os
import threading


genericEvent = USEREVENT + 1
randomEvent = USEREVENT + 2

pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size, pygame.DOUBLEBUF)
clock = pygame.time.Clock()
pygame.display.set_caption('Better timer demo')

timers = BetterTimers() #You need to define the BetterTimers object


timers.set_timer(pygame.event.Event(genericEvent, code="cool"), 500)
timers.set_timer(pygame.event.Event(genericEvent, code="uncool"), 1000)
timers.set_timer(pygame.event.Event(genericEvent, code="cool"), 2000)

timers.set_timer(randomEvent, 5000)
timers.set_timer(randomEvent, 0)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            running = False
            timers.end_all_timers() #We stop all the timers to be able to exit safely
            pygame.quit()
            break
        if event.type == randomEvent:
            print("WOWZERS")
        if event.type == genericEvent and event.code == 'cool':
            print("COOL EVENT")
        if event.type == genericEvent and event.code == 'uncool':
            print("SO UNCOOL")
    clock.tick(1000)  # It is good game design to try to limit the fps as little as possible.
pygame.quit()
