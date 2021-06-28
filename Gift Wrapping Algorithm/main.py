""" 
    Created on Mon May 17 2021

    @author: umairkarel
"""

import pygame
from pygame.draw import *
from random import randint
import numpy as np

width = 400
height = 400
white = (255,255,255)
black = (0,0,0)
pink = (255,0,220)
blue = (110, 173, 255)
w = 20

screen = pygame.display.set_mode((width, height))
screen.fill(white)
clock = pygame.time.Clock()
FPS = 60

points = []
for i in range(50):
    points.append([randint(10,width-10), randint(10,height-10)])
points.sort()

leftmost = points[0]
current = leftmost
index = 2
nxt = points[1]
hull = [leftmost]
done = False

def draw():
    global index,nxt,current,done

    for point in points:
        x = point[0]
        y = point[1]
        circle(screen, black, (x,y), 2)
    circle(screen, pink, (leftmost[0],leftmost[1]), 2)
    circle(screen, blue, (current[0],current[1]), 2)

    if not done:
        line(screen, pink, current, nxt, 1)

        check = points[index]
        line(screen, blue, current, check)

        a = np.subtract(nxt, current)
        b = np.subtract(check, current)
        c = np.cross(a,b)

        if c < 0:
            nxt = check

        index += 1

    if index == len(points):
        if nxt == leftmost:
            done = True
            hull.append(leftmost)
        else:
            current = nxt
            nxt = leftmost
            index = 0

            hull.append(current)

    for i in range(len(hull)-1):
        line(screen, black, hull[i], hull[i+1])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    screen.fill(white)
    draw()
    
    clock.tick(FPS)