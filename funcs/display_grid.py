## This function will be passed the gird, and it will print it nicely in the terminal
def print_grid(grid, generation):
    # Live ( 1 ) -> 1
    # Dead ( 0 ) -> -
    generation += 1
    display_grid = grid
    
    print(f'Generation number: {generation}')

    for row in range(len(display_grid)):
        for cell in range(len(display_grid[row])):
            if grid[row][cell] == 0:
                grid[row][cell] = '-'
            elif grid[row][cell] == 1:
                grid[row][cell] = '0'
        
            print(grid[row][cell], end='  ')
        print()
    
    print(end='\n\n\n')

    return generation
