""" 
    Created on Sat May 1 2021

    @author: umairkarel
"""

from setup import *

def removeWall(a, b):
    x = a.x - b.x
    y = a.y - b.y

    if y == 1:    # Top
        a.boundaries[0] = False
        b.boundaries[2] = False
    elif x == -1: # Right
        a.boundaries[1] = False
        b.boundaries[3] = False
    elif y == -1: # Bottom
        a.boundaries[2] = False
        b.boundaries[0] = False
    elif x == 1:  # Left
        a.boundaries[3] = False
        b.boundaries[1] = False

def draw():
    global current

    current.visited = True
    current.highlight()

    for i in range(rows):
        for j in range(cols):
            cells[i][j].show()
    

    nxt = current.getNeighbor()

    if nxt:
        stack.append(current)
        nxt.visited = True
        removeWall(current, nxt)
        current = nxt
    elif stack:
        current = stack.pop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    pygame.display.flip()
    screen.fill(white)
    clock.tick(FPS)

pygame.quit()