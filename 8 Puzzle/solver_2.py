""" 
    Created on Thu May 11 2021

    @author: umairkarel
"""

def copy(data):
    temp = []

    for i in data:
        t = []
        for j in i:
            t.append(j)
        temp.append(t)
    return temp
    
def find_blank(data):
    N = len(data)

    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                return (i,j)

def find_moves(data):
    x,y = find_blank(data)
    moves = []

    if (x != 0):
        moves.append((x-1,y))
    if (y != 0):
        moves.append((x,y-1))
    if (y != 2):
        moves.append((x,y+1))
    if (x != 2):
        moves.append((x+1,y))

    return moves, (x,y)

def neighbors(board):
    data, level = board
    neighbors = []
    moves, (x,y) = find_moves(data)

    for i,j in moves:
        state = copy(data)
        state[x][y], state[i][j] = state[i][j], state[x][y]
        neighbors.append([state, level+1, 0])

    return neighbors

def hueristic(board, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] and board[i][j] != goal[i][j]:
                count += 1

    return count


def solve(board):
    openSet.append([board, 0, 0])
    step = 0
    while len(openSet) > 0:
        curr = openSet[0]

        print("step: ", step)
        step += 1
        for i in curr[0]:
            for j in i:
                print(j,end=" ")
            print("")
        print("")

        if hueristic(openSet[0][0], goal) == 0:
            break

        closedSet.append(curr[0])
        openSet.remove(curr)

        # for neighbor in neighbors(curr[:2]):
        #     # neighbor[2] = hueristic(neighbor[0], goal) + neighbor[1]
        #     neighbor[2] = hueristic(neighbor[0], goal) # Best First Search
        #     openSet.append(neighbor)

        for neighbor in neighbors(curr[:2]):
            if neighbor[0] not in closedSet:
                neighbor[2] = hueristic(neighbor[0], goal) # Best First Search
                openSet.append(neighbor)

        openSet.sort(key = lambda x:x[2],reverse=False)

start = [[8,6,7],
         [2,5,4],
         [3,0,1]]

goal  = [[1,2,3],
         [4,5,6],
         [7,8,0]]

openSet = []
closedSet = []

solve(start)