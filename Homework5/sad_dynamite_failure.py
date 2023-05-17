def print_maze_dp():
    for row in maze_dp:
        for element in row:
            print(element, end="")
            for _ in range(10 - (len(str(element[0])) + len(str(element[1])))):
                print(end=" ")
        print()
    print()

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
        # walls are not considered connected to other walls, since there's only one stick of dynamite and travelling through two walls is impossible
        if i > 0: # add tile above
            if not (maze[i][j] == 1 and maze[i - 1][j] == 1):
                adjacencies[i][j].append((i - 1, j))
        if i < d1 - 1: # add tile below
            if not (maze[i][j] == 1 and maze[i + 1][j] == 1):
                adjacencies[i][j].append((i + 1, j))
        if j > 0: # add tile left
            if not (maze[i][j] == 1 and maze[i][j - 1] == 1):
                adjacencies[i][j].append((i, j - 1))
        if j < d2 - 1: # add tile right
            if not (maze[i][j] == 1 and maze[i][j + 1] == 1):
                adjacencies[i][j].append((i, j + 1))

# initialize dynamic programming d1 x d2 array, where each element is a size 2 list
# the first element in the list is the shortest path from the start to i,j without dynamite, the second element is with dynamite
maze_dp = [[[float('inf'), float('inf')] for _ in range(d2)] for _ in range(d1)]
maze_dp[0][0] = [0, 0] # the shortest path to the start is 0 without dynamite, and dynamite can't have been used yet

# first, find the shortest path to anywhere that can be accessed without dynamite
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

# next, find the shortest path to anywhere using a single stick of dynamite
visited = [[False for _ in range(d2)] for _ in range(d1)] # 2D array that tracks whether each tile in the maze has been visited
visited[0][0] = True # skip the first tile

delays = [[-1 for _ in range(d2)] for _ in range(d1)] # delays paths equal to how much a move is "skipping" to preserve BFS always finding the shortest path

queue = [(1, 0), (0, 1)] # element represents a tuple of the row,column of a tile in the maze
while len(queue) > 0:
    tile = queue.pop(0) # O(1) operation
    if delays[tile[0]][tile[1]] > 0:
        delays[tile[0]][tile[1]] -= 1
        queue.append(tile)
        continue

    # visit each adjacent tile, add it to adjacent_paths, and add it to the queue if it hasn't been visited
    adjacent_paths_no_dynamite = []
    adjacent_paths_dynamite = []
    adjacent_paths_coords = []
    for adj_tile in adjacencies[tile[0]][tile[1]]:
        adjacent_paths_no_dynamite.append(maze_dp[adj_tile[0]][adj_tile[1]][0] + 1)
        adjacent_paths_dynamite.append(maze_dp[adj_tile[0]][adj_tile[1]][1] + 1)
        adjacent_paths_coords.append((adj_tile[0], adj_tile[1]))

    # if this tile is a wall, there is no path there without dynamite
    if maze[tile[0]][tile[1]] == 1:
        min_adj_index = 0
        for i in range(len(adjacent_paths_no_dynamite)):
            if adjacent_paths_no_dynamite[i] < adjacent_paths_no_dynamite[min_adj_index]:
                min_adj_index = i

        maze_dp[tile[0]][tile[1]][1] = adjacent_paths_no_dynamite[min_adj_index]
        if delays[tile[0]][tile[1]] == -1:
            if adjacent_paths_no_dynamite[min_adj_index] != float('inf'):
                delays[tile[0]][tile[1]] = adjacent_paths_no_dynamite[min_adj_index] - maze_dp[adjacent_paths_coords[min_adj_index][0]][adjacent_paths_coords[min_adj_index][1]][1] - 1
                queue.append(tile)
                continue
            else:
                delays[tile[0]][tile[1]] = 0
                continue
    else:
        maze_dp[tile[0]][tile[1]][1] = min(adjacent_paths_dynamite)
    
    for adj_tile in adjacencies[tile[0]][tile[1]]:
        if not visited[adj_tile[0]][adj_tile[1]]:
            visited[adj_tile[0]][adj_tile[1]] = True
            queue.append((adj_tile[0], adj_tile[1]))

for row in maze_dp:
    print(row)

print(maze_dp[d1 - 1][d2 - 1][1]) # solution is in the bottom right because the exit is in the bottom right