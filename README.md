# Game of life
This is a simple game, it is played on a grid. Each square in the grid can be either alive or dead. There are a couple of rules that will decide if a cell dies or survives:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Todo's
1. Add a simple user interface so that the user can choose which cells are alive at the start without chaning any code.
2. Make the printed text update instead of printing a new line every time.
