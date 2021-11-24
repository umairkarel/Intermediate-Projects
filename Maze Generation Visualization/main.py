""" 
    Created on Sat May 1 2021
    Updated on Mon Aug 9 2021

    @author: umairkarel
"""
from setup import *
from solver import solve

def removeWall(a, b):
    x = a.x - b.x
    y = a.y - b.y

    # Top
    if y == 1:    
        a.boundaries[0] = False
        b.boundaries[2] = False
    # Right
    elif x == -1: 
        a.boundaries[1] = False
        b.boundaries[3] = False
    # Bottom
    elif y == -1: 
        a.boundaries[2] = False
        b.boundaries[0] = False
    # Left
    elif x == 1:  
        a.boundaries[3] = False
        b.boundaries[1] = False

def traverse():
    global i,path

    if i < len(path):
        x,y = path[i]
        player.move(x, y, True)
        player.show()
    else:
        path = None
        i = 0
    i += 1

def draw():
    global current, path, player

    current.visited = True
    current.highlight(True)

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
    else:
        current.highlight(False)
        if not player:
            player = Player(0,0)
        if player.win():
            player.show(pink)
        else:
            player.show()

path = None
running = True
i = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if player:
                if event.key == pygame.K_UP:
                    player.move(0,-1)
                if event.key == pygame.K_RIGHT:
                    player.move(1,0)
                if event.key == pygame.K_DOWN:
                    player.move(0,1)
                if event.key == pygame.K_LEFT:
                    player.move(-1,0)

            if event.key == pygame.K_RETURN:
                path = solve(cells, player.x, player.y)

    draw()
    if path:
        traverse()

    pygame.display.flip()
    screen.fill(white)
    clock.tick(FPS)

pygame.quit()