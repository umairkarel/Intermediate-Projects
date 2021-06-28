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
off_white = (220,220,220)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255, 213, 128)

# Const
pygame.font.init()
fnt = pygame.font.SysFont("comicsans", 50)
width = 500
height = 500
screen = pygame.display.set_mode((width,height))
screen.fill(off_white)
clock = pygame.time.Clock()
FPS = 60
N = 10
w = width // N

class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.prev = None
        self.obstacle = False

    def addNeighbors(self, adj=True, diag=True):
        self.neighbors = []
        i = self.x
        j = self.y

        if adj:
            if i < N-1:
                self.neighbors.append(board[i+1][j])
            if i > 0:
                self.neighbors.append(board[i-1][j])
            if j < N-1:
                self.neighbors.append(board[i][j+1])
            if j > 0:
                self.neighbors.append(board[i][j-1])

        if diag:
            if i > 0 and j > 0 and not(board[i-1][j].obstacle or board[i][j-1].obstacle):
                self.neighbors.append(board[i-1][j-1])

            if i < N-1 and j > 0 and not(board[i+1][j].obstacle or board[i][j-1].obstacle):
                self.neighbors.append(board[i+1][j-1])

            if i > 0 and j < N-1 and not(board[i-1][j].obstacle or board[i][j+1].obstacle):
                self.neighbors.append(board[i-1][j+1])

            if i < N-1 and j < N-1 and not(board[i+1][j].obstacle or board[i][j+1].obstacle):
                self.neighbors.append(board[i+1][j+1])


    def show(self, color, fill):
        global screen, w

        x1, y1 = self.y*w, self.x*w
        pygame.draw.rect(screen, color, pygame.Rect(x1,y1,w,w), fill)


def init_neighbors():
    for i in range(N):
        for j in range(N):
            board[i][j].addNeighbors(True,False)

def init_obstacle(n):
    for i in range(n):
        x = random.randint(0, N-1)
        y = random.randint(0, N-1)
        board[x][y].obstacle = True

def heuristic(a,b):
    d = math.dist((a.x,a.y), (b.x,b.y)) # Euclidean
    # d = abs(a.x - b.x) + abs(a.y - b.y) # Manhattan
    return d

def draw():
    for i in range(N):
        for j in range(N):
            if board[i][j].obstacle:
                board[i][j].show(black, 0)
            else:
                board[i][j].show(black, 1)

    for i in range(len(openSet)):
        openSet[i].show(yellow, 0)

    for i in range(len(closedSet)):
        closedSet[i].show(white, 0)
        closedSet[i].show(black, 1)

    if not noSoln:
        drawPath()

def drawPath():
    path = []
    temp = curr
    path.append(temp)

    while temp.prev:
        path.append(temp.prev)
        temp = temp.prev

    for i in range(len(path)):
        path[i].show(blue, 0)

def a_star():
    global curr, noSoln
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
            if neighbor not in closedSet and not neighbor.obstacle:
                gScore = curr.g + 1
                
                newPath = False
                if neighbor in openSet:
                    if gScore < neighbor.g:
                        neighbor.g = gScore
                        newPath = True
                        
                else:
                    neighbor.g = gScore
                    openSet.append(neighbor)
                    newPath = True

                if newPath:
                    neighbor.h = heuristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.prev = curr
    else:
        noSoln = True

board = [[Spot(i,j) for j in range(N)] for i in range(N)]
start = board[0][0]
end = board[N-1][N-1]
openSet = [start]
closedSet = []
curr = start
noSoln = False
solve = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                solve = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < width and pos[1] < height:
                gap = width // N
                x = pos[1] // gap
                y = pos[0] // gap
                board[x][y].obstacle = True
                init_neighbors()

    if solve:
        a_star()

    draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()