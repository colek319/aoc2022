from lib.lib import readlines

def part1():
    visited = set()
    knots = [(0,0)] * 2
    lines = readlines('08')
    for line in lines:
        d, m = line.split(' ')
        for _ in range(int(m)):
            for i in range(len(knots)):
                move(knots, i, d)
            visited.add(knots[-1])
    print(len(visited))

def part2():
    visited = set()
    knots = [(0,0)] * 10
    lines = readlines('08')
    for line in lines:
        d, m = line.split(' ')
        for _ in range(int(m)):
            for i in range(len(knots)):
                move(knots, i, d)
            visited.add(knots[-1])                
    print(len(visited))

# where d is direction
def move(knots, i, d):
    head = knots[i - 1]
    tail = knots[i]

    # move head
    if i == 0:
        if d == 'L':
            knots[0] = (knots[0][0] - 1, knots[0][1])
        elif d == 'R':
            knots[0] = (knots[0][0] + 1, knots[0][1])
        elif d == 'U':
            knots[0] = (knots[0][0], knots[0][1] + 1)
        elif d == 'D':
            knots[0] = (knots[0][0], knots[0][1] - 1)        
        return 

    # # check if we need to move
    # if (head[0] == tail[0] and head[1] == tail[1]):
    #     # same spot
    #     return
    # elif (head[0] == tail[0] and head[1] == tail[1] + 1):
    #     # up 1
    #     return
    # elif (head[0] == tail[0] and head[1] == tail[1] - 1):
    #     # down 1
    #     return
    # elif (head[0] == tail[0] + 1 and head[1] == tail[1]):
    #     # right 1
    #     return
    # elif (head[0] == tail[0] - 1 and head[1] == tail[1]):
    #     # left 1
    #     return
    # elif (head[0] == tail[0] + 1 and head[1] == tail[1] + 1):
    #     # up right
    #     return
    # elif (head[0] == tail[0] - 1 and head[1] == tail[1] + 1):
    #     # up left
    #     return
    # elif (head[0] == tail[0] + 1 and head[1] == tail[1] - 1):
    #     # down right
    #     return
    # elif (head[0] == tail[0] - 1 and head[1] == tail[1] - 1):
    #     # down left
    #     return

    # apply rules
    # up right
    if head[1] >= tail[1] + 1 and head[0] >= tail[0] + 1 and (head[1] != tail[1] + 1 or head[0] != tail[0] + 1):
        knots[i] = (tail[0] + 1, tail[1] + 1)
    # up left
    elif head[1] >= tail[1] + 1 and head[0] <= tail[0] - 1 and (head[1] != tail[1] + 1 or head[0] != tail[0] - 1):
        knots[i] = (tail[0] - 1, tail[1] + 1)
    # down right
    elif head[1] <= tail[1] - 1 and head[0] >= tail[0] + 1 and (head[1] != tail[1] - 1 or head[0] != tail[0] + 1):
        knots[i] = (tail[0] + 1, tail[1] - 1)
    # down left
    elif head[1] <= tail[1] - 1 and head[0] <= tail[0] - 1 and (head[1] != tail[1] - 1 or head[0] != tail[0] - 1):
        knots[i] = (tail[0] - 1, tail[1] - 1)
    # up up
    elif tail[1] + 2 == head[1]:
        knots[i] = (tail[0], tail[1] + 1)
    # right right
    elif tail[0] + 2 == head[0]:
        knots[i] = (tail[0] + 1, tail[1])
    # down down
    elif tail[1] - 2 == head[1]:
        knots[i] = (tail[0], tail[1] - 1)
    # left left
    elif tail[0] - 2 == head[0]:
        knots[i] = (tail[0] - 1, tail[1])        

def printknots(knots):
    vis = [['.'] * 6 for _ in range(6)]
    for i in range(len(knots) - 1, -1, -1):
        vis[knots[i][0]][knots[i][1]] = i if i != 0 else 'H'
    for i in range(6):
        for j in range(6):
            print(vis[j][5 - i], end='')
        print()

def printvisited(visited):
    for i in range(40):
        for j in range(40):
            if (i,j) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()



if __name__ == '__main__':
    part1()
    part2()