'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

def islandPerimeter1(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell == 1:
                cell_size = 0
                if i == 0:
                    cell_size += 1
                else:
                    top_cell = grid[i-1][j]
                    if top_cell == 0:
                        cell_size += 1
                # left side
                if j == 0:
                    cell_size += 1
                else:
                    left_cell = grid[i][j-1]
                    if left_cell == 0:
                        cell_size += 1
                # right side
                if j < cols -1:
                    right_cell = grid[i][j+1]
                    if right_cell == 0:
                        cell_size += 1
                else:
                    cell_size += 1
                # bottom
                if i < rows -1:
                    bottom_cell = grid[i+1][j]
                    if bottom_cell == 0:
                        cell_size += 1
                else:
                    cell_size += 1
                perimeter += cell_size
                print i, j, cell_size      
        print i, perimeter      
    print perimeter


def islandPerimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                perimeter += 4
                if i > 0 and grid[i-1][j]:
                    perimeter -= 2
                if j > 0 and grid[i][j-1]:
                    perimeter -= 2
    return perimeter

grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
print islandPerimeter(grid)
grid = [[1]]
print islandPerimeter(grid)

