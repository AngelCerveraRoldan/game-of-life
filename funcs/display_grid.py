## This function will be passed the gird, and it will print it nicely in the terminal
def print_grid(grid):
    # Live ( 1 ) -> 1
    # Dead ( 0 ) -> -
    
    display_grid = grid
    
    for row in range(len(display_grid)):
        for cell in range(len(display_grid[row])):
            if grid[row][cell] == 0:
                grid[row][cell] = '-'
            elif grid[row][cell] == 1:
                grid[row][cell] = '0'
        
            print(grid[row][cell], end='  ')
        print()
