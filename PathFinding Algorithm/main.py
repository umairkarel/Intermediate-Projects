""" 
    Created on Mon March 15 2021

    @author: umairkarel
"""

import pygame
import random
from board import Board
import math

# Colors
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

# Const
pygame.font.init()
fnt = pygame.font.SysFont("comicsans", 50)
width = 300
height = 300
screen = pygame.display.set_mode((width,height))
screen.fill(white)
clock = pygame.time.Clock()
FPS = 30
n = 25
w = width // n

class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.prev = None

    def addNeighbors(self):
        i = self.x
        j = self.y

        if i < n-1:
            self.neighbors.append(board[i+1][j])
        if i > 0:
            self.neighbors.append(board[i-1][j])
        if j < n-1:
            self.neighbors.append(board[i][j+1])
        if j > 0:
            self.neighbors.append(board[i][j-1])

    def show(self, color, fill):
        global width, screen, w

        x1, y1 = self.y*w, self.x*w
        width, height = w, w
        pygame.draw.rect(screen, color, pygame.Rect(x1,y1,width,height), fill)


board = [[Spot(i,j) for j in range(n)] for i in range(n)]
start = board[0][0]
end = board[n-1][n-1]
openSet = [start]
closedSet = []
curr = None

for i in range(n):
    for j in range(n):
        board[i][j].addNeighbors()

def heuristic(a,b):
    # d = math.dist((a.x,a.y), (b.x,b.y)) # Euclidean
    d = abs(a.x - b.x) + abs(a.y - b.y) # Manhattan
    return d

def draw():
    for i in range(n):
        for j in range(n):
            board[i][j].show(black, 1)

    for i in range(len(openSet)):
        openSet[i].show(green, 0)

    for i in range(len(closedSet)):
        closedSet[i].show(red, 0)

    path = []
    temp = curr
    path.append(temp)
    while temp.prev:
        path.append(temp.prev)
        temp = temp.prev

    for i in range(len(path)):
        path[i].show(blue, 0)

def a_star():
    global curr
    if len(openSet) > 0:
        low = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[low].f:
                low = i

        curr = openSet[low]
        if curr == end:
            return

        openSet.remove(curr)
        closedSet.append(curr)

        for neighbor in curr.neighbors:
            if neighbor not in closedSet:
                gScore = curr.g + 1
                
                if neighbor in openSet:
                    if gScore < neighbor.g:
                        neighbor.g = gScore
                        
                else:
                    neighbor.g = gScore
                    openSet.append(neighbor)

                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.prev = curr
    else:
        return

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    a_star()
    draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



# Logic
# -> While openSet is not Empty - Declaration (openSet, closedSet)


#######
# if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RETURN:
        #         board.set_model()
            
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     placed = board.place(pos)

############################################
# neighbors = curr.neighbors
# for i in range(len(neighbors)):
#     neighbor = neighbors[i]
# print(curr.neighbors)
# for neighbor in curr.neighbors:
#     if neighbor in closedSet:
#         continue
#     gScore = curr.g + 1
#     if gScore < neighbor.g:
#         neighbor.g = gScore
#         neighbor.h = heuristic(neighbor, end)
#         neighbor.f = neighbor.g + neighbor.h
#         if neighbor not in openSet:
#             openSet.append(neighbor)