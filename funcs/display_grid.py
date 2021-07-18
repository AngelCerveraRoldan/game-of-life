## This function will be passed the gird, and it will print it nicely in the terminal
def print_grid(grid):
    # Live ( 1 ) -> 1
    # Dead ( 0 ) -> -
    display_grid = grid
    
    for row in range(len(display_grid)):

        for cell in range(len(display_grid[row])):

            if display_grid[row][cell] == 0:
                print('-', end='  ')

            elif display_grid[row][cell] == 1:
                print('0', end='  ')
        
        print()
    
    print(end='\n\n\n')
