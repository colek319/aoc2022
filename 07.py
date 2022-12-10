from lib.lib import readlines

WIDTH = 99
HEIGHT = 99

def part1():
    visible = 0
    forest = readlines('07')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if is_visible(forest, i, j):
                visible += 1
    print(visible)

def part2():
    max_vis = 0
    forest = readlines('07')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            score = visibility_score(forest, i, j)
            print(score)
            max_vis = max(max_vis, score)
    print(max_vis)

def visibility_score(forest, row, col):
    if row == 0:
        return 0
    if col == 0:
        return 0
    if row == HEIGHT - 1:
        return 0
    if col == WIDTH - 1:
        return 0
    
    tree_height = forest[row][col]

    # visible from left
    vis_left = 0
    for c in range(col - 1, -1, -1):
        vis_left += 1        
        if forest[row][c] >= tree_height:
            break

    # visible from right
    vis_right = 0
    for c in range(col + 1, WIDTH, 1):
        vis_right += 1
        if forest[row][c] >= tree_height:
            break      

    # visible from up
    vis_up = 0  
    for r in range(row - 1, -1, -1):
        vis_up += 1  
        if forest[r][col] >= tree_height:
            break    

    # visible from down
    vis_down = 0  
    for r in range(row + 1, HEIGHT, 1):
        vis_down += 1        
        if forest[r][col] >= tree_height:
            break       

    return vis_left * vis_right * vis_up * vis_down    


def is_visible(forest, row, col):
    if row == 0:
        return True
    if col == 0:
        return True
    if row == HEIGHT - 1:
        return True
    if col == WIDTH - 1:
        return True
    
    tree_height = forest[row][col]

    # visible from left
    visible = True    
    for c in range(col - 1, -1, -1):
        if forest[row][c] >= tree_height:
            visible = False
    if visible:
        return True

    # visible from right
    visible = True
    for c in range(col + 1, WIDTH, 1):
        # print(c)
        if forest[row][c] >= tree_height:
            visible = False    
    if visible:
        return True        

    # visible from up
    visible = True    
    for r in range(row - 1, -1, -1):
        if forest[r][col] >= tree_height:
            visible = False      
    if visible:
        return True         

    # visible from down
    visible = True    
    for r in range(row + 1, HEIGHT, 1):
        if forest[r][col] >= tree_height:
            visible = False   
    if visible:
        return True        

    return False
    


if __name__ == '__main__':
    part1()
    part2()