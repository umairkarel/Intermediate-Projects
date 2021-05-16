import pygame
from pygame.draw import *
from random import randint, choice
from cell import Cell

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

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boundaries = [True,True,True,True]
        self.visited = False

    def getNeighbor(self):
        i = self.x
        j = self.y
        neighbors = []
        n = cols

        top    = cells[i][j-1] if j > 0 else 0
        right  = cells[i+1][j] if i < cols-1 else 0
        bottom = cells[i][j+1] if j < rows-1 else 0
        left   = cells[i-1][j] if i > 0 else 0

        if top    and not top.visited:
            neighbors.append(top)

        if right  and not right.visited:
            neighbors.append(right)

        if bottom and not bottom.visited:
            neighbors.append(bottom)

        if left   and not left.visited:
            neighbors.append(left)

        if neighbors:
            return choice(neighbors)
        else:
            return None

    def highlight(self):
        x, y = self.x*w, self.y*w

        rect(screen, blue, pygame.Rect(x+1,y+1,w-1,w-1), 0)

    def show(self):
        x, y = self.x*w, self.y*w

        if self.boundaries[0]:
            line(screen, black, (x, y), (x+w, y))     # Top
        if self.boundaries[1]:
            line(screen, black, (x+w, y), (x+w, y+w)) # Right
        if self.boundaries[2]:
            line(screen, black, (x, y+w), (x+w, y+w)) # Bottom
        if self.boundaries[3]:
            line(screen, black, (x, y), (x, y+w))     # Left


cols = width//w
rows = height//w
cells = []
for i in range(rows):
    cell_list = []
    for j in range(cols):
        cell_list += [Cell(i, j)]
    cells += [cell_list]

current = cells[0][0]
stack = []