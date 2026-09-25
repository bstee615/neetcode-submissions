def printgrid(grid):
    for row in grid:
        for cell in row:
            print(cell + " ", end="")
        print()
    print("\n\n")

def search(grid, i, j):
    # call recursively
    # for each cell, mark it 0 and search all neighbors
    # print(i, j)
    # printgrid(grid)
    grid[i][j] = "0"
    jmod = 0
    for imod in [-1, 1]:
        # print("imod", i, j, imod, jmod, len(grid), len(grid[i]), i+imod < 0, i+imod >= len(grid), j+jmod < 0, j+jmod >= len(grid[i+imod]))
        if i+imod < 0 or i+imod >= len(grid):
            continue
        if grid[i+imod][j] == "1":
            search(grid, i+imod, j)
    imod = 0
    for jmod in [-1, 1]:
        # print("jmod", i, j, imod, jmod, i+imod < 0, i+imod >= len(grid), j+jmod < 0, j+jmod >= len(grid[i+imod]))
        if j+jmod < 0 or j+jmod >= len(grid[i]):
            continue
        if grid[i][j+jmod] == "1":
            search(grid, i, j+jmod)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Each 1 belongs to only one island.
        # Once we see a 1, we know that any contiguous cell is part of the same island.

        # iterate TD LR. Each time we find a 1, search all contiguous 1's and mark them, and increment a counter. Return when the TD LR iteration is done.
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    search(grid, i, j)
                    num_islands += 1
                    print("ISLAND", num_islands)
        return num_islands
