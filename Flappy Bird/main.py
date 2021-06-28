""" 
    Created on Mon April 19 2021

    @author: umairkarel
"""

import pygame
from pygame.draw import *
from random import randint

width = 300
height = 400
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 60

class Bird:
    def __init__(self):
        self.x = 80
        self.y = height//2
        self.r = 9
        self.gravity = 0.4
        self.velocity = 0
        self.uplift = -12

    def show(self):
        self.x = int(self.x)
        self.y = int(self.y)
        circle(screen, white, (self.x,self.y), self.r)

    def flapp(self):
        self.velocity += self.uplift

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity * 0.9

        if self.y > height-self.r:
            self.y = height-self.r
            self.velocity = 0

        elif self.y < self.r:
            self.y = self.r
            self.velocity = 0

class Obstacle:
    def __init__(self):
        self.top = randint(0,(height//2)-25)
        self.bottom = randint(0,(height//2)-25)
        self.x = 300
        self.w = 20
        self.hit = False

    def show(self):
        color = red if self.hit else white
        rect(screen, color, pygame.Rect(self.x,0,self.w,self.top))
        rect(screen, color, pygame.Rect(self.x,height-self.bottom,self.w,height))

    def update(self):
        self.x -= 2

    def hits(self, bird):
        if (bird.y < self.top or bird.y > height-self.bottom):
            if (bird.x > self.x and bird.x < self.x + self.w):
                self.hit = True
                return
        self.hit = False 

bird = Bird()
pipes = [Obstacle()]

running = True
frameCount = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flapp()

    if frameCount%100 == 0:
        pipes.append(Obstacle())

    for pipe in pipes:
        pipe.hits(bird)

        pipe.show()
        pipe.update()

        if pipe.x < -pipe.w:
            pipes.remove(pipe)
        

    bird.show()
    bird.update()

    pygame.display.flip()
    screen.fill(black)
    clock.tick(FPS)
    frameCount += 1

pygame.quit()