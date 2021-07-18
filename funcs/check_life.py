## This function will be passed the grid, it will then check the surrounding cells of every cell
def life(grid):
    ## This 2 lists will show which cells need to be changed from life to death and from death to life. [row, cell]
    alive = []
    new_grid = []

    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            surr_alive = check_around(grid, row, cell)

            if surr_alive == 3:
                ## Cell lives on
                alive.append([row, cell])

            if grid[row][cell] == 1 and surr_alive == 2:
                alive.append([row, cell])

    ## Create a new grid of the same size with all 0's
    for i in range(len(grid)):
        new_grid.append([])

        for u in range(len(grid[0])):
            new_grid[i].append(0)

    ## Add 1's
    for x in alive:
        new_grid[x[0]][x[1]] = 1

    return new_grid


def check_around(grid, row, cell):
    a = 0

    ## Check row above
    if check_cell(grid, row - 1, cell - 1) == True:
        a += 1
    if check_cell(grid, row - 1, cell) == True:
        a += 1
    if check_cell(grid, row - 1, cell + 1) == True:
        a += 1   

    ## Check right and left
    if check_cell(grid, row, cell - 1) == True:
        a += 1
    if check_cell(grid, row, cell + 1) == True:
        a += 1

    ## Check row below
    if check_cell(grid, row + 1, cell - 1) == True:
        a += 1
    if check_cell(grid, row + 1, cell) == True:
        a += 1
    if check_cell(grid, row + 1, cell + 1) == True:
        a += 1


    return a


def check_cell(grid, row, cell):
    ## Check if grid[row][cell] exists
    if row >= len(grid) or row < 0 or cell >= len(grid[0]) or cell < 0:
        return False
    elif grid[row][cell] == 1:
        return True
    else:
        return False