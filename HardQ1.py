def create_grid(n):
    grid = []

    # create n x n grid filled with 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1)
        grid.append(row)

    return grid

def add_obstacles(grid, obstacles):
    n = len(grid)

    for obs in obstacles:
        north = obs[0]
        east = obs[1]
        south = obs[2]
        west = obs[3]

        # mark obstacles (check bounds)
        if north < n:
            grid[north][0] = 0

        if east < n:
            grid[0][east] = 0

        if south < n:
            grid[n-1][south] = 0

        if west < n:
            grid[west][n-1] = 0



def shortest_path(grid):
    n = len(grid)

    queue = []
    visited = []

    # start from (0,0)
    queue.append([0, 0, 0])  # row, col, distance
    visited.append((0, 0))

    while len(queue) > 0:
        current = queue.pop(0)

        row = current[0]
        col = current[1]
        dist = current[2]

        # if reached destination
        if row == n-1 and col == n-1:
            return dist

        # move in 4 directions
        moves = [[1,0], [-1,0], [0,1], [0,-1]]

        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]

            # check valid position
            if 0 <= new_row < n and 0 <= new_col < n:
                if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    queue.append([new_row, new_col, dist + 1])
                    visited.append((new_row, new_col))

    return -1

def print_grid(grid):
    for row in grid:
        print(row)

# input
n = int(input("Enter n:"))
obstacles =eval(input("Enter the obstacles:"))
# create grid
grid = create_grid(n)

# add obstacles
add_obstacles(grid, obstacles)

# print grid
print("Grid:")
print_grid(grid)

# find shortest path
result = shortest_path(grid)

print("Shortest path:", result)