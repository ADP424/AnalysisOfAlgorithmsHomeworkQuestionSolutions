d1 = int(input())
d2 = int(input())

maze = [] # 2D array that represents the input maze layout
for i in range(d1):
    maze.append([int(i) for i in input().split(' ')])

adjacencies = [] # 2D array parallel to the maze array with all adjacenies to that tile
for i in range(d1):
    adjacencies.append([])
    for j in range(d2):
        adjacencies[i].append([])
        # walls are considered adjacent to everything
        if maze[i][j] == 1:
            if i > 0: # add tile above
                adjacencies[i][j].append((i - 1, j))
            if i < d1 - 1: # add tile below
                adjacencies[i][j].append((i + 1, j))
            if j > 0: # add tile left
                adjacencies[i][j].append((i, j - 1))
            if j < d2 - 1: # add tile right
                adjacencies[i][j].append((i, j + 1))
        # paths are not considered adjacent to walls (0s not adjacent to 1s)
        else:
            if i > 0: # add tile above
                if not (maze[i - 1][j] == 1):
                    adjacencies[i][j].append((i - 1, j))
            if i < d1 - 1: # add tile below
                if not (maze[i + 1][j] == 1):
                    adjacencies[i][j].append((i + 1, j))
            if j > 0: # add tile left
                if (not maze[i][j - 1] == 1):
                    adjacencies[i][j].append((i, j - 1))
            if j < d2 - 1: # add tile right
                if not (maze[i][j + 1] == 1):
                    adjacencies[i][j].append((i, j + 1))

# initialize dynamic programming d1 x d2 array, where each element is a size 2 list
# the first element in the list is the shortest path from the start to i,j without dynamite, the second element is the shortest path from the end to i,j without dynamite
maze_dp = [[[float('inf'), float('inf')] for _ in range(d2)] for _ in range(d1)]

# first, find the shortest path to anywhere that can be accessed without dynamite from the start
maze_dp[0][0] = [0, float('inf')] # the shortest path to the start is 0
visited = [[False for _ in range(d2)] for _ in range(d1)] # 2D array that tracks whether each tile in the maze has been visited
visited[0][0] = True # skip the first tile

queue = [(1, 0), (0, 1)] # each element is a tuple of the form (row,column) of a tile in the maze
while len(queue) > 0:
    tile = queue.pop(0) # O(1) operation

    # visit each adjacent tile, add it to adjacent_paths, and add it to the queue if it hasn't been visited
    adjacent_paths = []
    for adj_tile in adjacencies[tile[0]][tile[1]]:
        adjacent_paths.append(maze_dp[adj_tile[0]][adj_tile[1]][0] + 1)
        if not visited[adj_tile[0]][adj_tile[1]] and maze[tile[0]][tile[1]] != 1:
            visited[adj_tile[0]][adj_tile[1]] = True
            queue.append(adj_tile)

    # if this tile is a wall, there is no path there without dynamite
    if maze[tile[0]][tile[1]] == 1:
        maze_dp[tile[0]][tile[1]][0] = float('inf')
    else:
        maze_dp[tile[0]][tile[1]][0] = min(adjacent_paths)

# next, find the shortest path to anywhere that can be accessed without dynamite from the end
maze_dp[-1][-1] = [float('inf'), 0] # the shortest path to the end is 0 starting from the end
visited = [[False for _ in range(d2)] for _ in range(d1)] # 2D array that tracks whether each tile in the maze has been visited
visited[-1][-1] = True # skip the last tile

queue = [(len(maze) - 2, len(maze[0]) - 1), (len(maze) - 1, len(maze[0]) - 2)] # each element is a tuple of the form (row,column) of a tile in the maze
while len(queue) > 0:
    tile = queue.pop(0) # O(1) operation

    # visit each adjacent tile, add it to adjacent_paths, and add it to the queue if it hasn't been visited
    adjacent_paths = []
    for adj_tile in adjacencies[tile[0]][tile[1]]:
        adjacent_paths.append(maze_dp[adj_tile[0]][adj_tile[1]][1] + 1)
        if not visited[adj_tile[0]][adj_tile[1]] and maze[tile[0]][tile[1]] != 1:
            visited[adj_tile[0]][adj_tile[1]] = True
            queue.append(adj_tile)

    # if this tile is a wall, there is no path there without dynamite
    if maze[tile[0]][tile[1]] == 1:
        maze_dp[tile[0]][tile[1]][1] = float('inf')
    else:
        maze_dp[tile[0]][tile[1]][1] = min(adjacent_paths)

# now find the wall with the smallest adjacent path from start and path from end
total_path_lengths = []
for i in range(d1):
    for j in range(d2):
        if maze[i][j] == 1:
            for adj_tile1 in adjacencies[i][j]:
                for adj_tile2 in adjacencies[i][j]:
                    if adj_tile1 != adj_tile2:
                        total_path_lengths.append(maze_dp[adj_tile1[0]][adj_tile1[1]][0] + maze_dp[adj_tile2[0]][adj_tile2[1]][1] + 2)

for row in maze_dp:
    print(row)
print(min(total_path_lengths))