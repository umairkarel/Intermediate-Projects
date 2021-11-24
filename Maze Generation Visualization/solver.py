""" 
    Created on Mon Aug 9 2021

    @author: umairkarel
"""
import math

class Spot:
    def __init__(self, x, y, boundaries):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.boundaries = boundaries
        self.prev = None

    def addNeighbor(self):
        i = self.x
        j = self.y
        neighbors = []

        top    = board[i][j-1] if j > 0 else 0
        right  = board[i+1][j] if i < N-1 else 0
        bottom = board[i][j+1] if j < N-1 else 0
        left   = board[i-1][j] if i > 0 else 0

        if not self.boundaries[0] and top:
            neighbors.append(top)

        if not self.boundaries[1] and right:
            neighbors.append(right)

        if not self.boundaries[2] and bottom:
            neighbors.append(bottom)

        if not self.boundaries[3] and left:
            neighbors.append(left)

        self.neighbors = neighbors

def init_neighbors():
    for i in range(N):
        for j in range(N):
            board[i][j].addNeighbor()

def heuristic(a,b):
    d = math.dist((a.x,a.y), (b.x,b.y)) # Euclidean
    # d = abs(a.x - b.x) + abs(a.y - b.y) # Manhattan
    return d

def getPath():
    path = []
    temp = curr
    path.insert(0, [temp.x,temp.y])

    while temp.prev:
        path.insert(0, [temp.prev.x, temp.prev.y])
        temp = temp.prev

    return path

curr = None
N = None
board = None

def solve(cells, start_x, start_y):
    global curr,board,N

    N = len(cells)
    board = [[Spot(i, j, cells[i][j].boundaries) for j in range(N)] for i in range(N)]
    start = board[start_x][start_y]
    curr = start
    end = board[N-1][N-1]
    openSet = [start]
    closedSet = []

    init_neighbors()
    while len(openSet) > 0:
        low = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[low].f:
                low = i

        curr = openSet[low]
        if curr == end:
            break

        openSet.remove(curr)
        closedSet.append(curr)
        for neighbor in curr.neighbors:
            if neighbor not in closedSet:
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

    return getPath()