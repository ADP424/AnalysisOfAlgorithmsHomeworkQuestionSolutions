# edges and vertices list
x = [int(x) for x in input().strip().split()]

num_vertices = x[0]
num_edges = x[1]

# list of unreliable nodes
input()
unreliables = [int(x) for x in input().strip().split()]
node_unreliable = [False for _ in range(num_vertices)] # each element represents [unreliable or not, has an edge attached or not]
for i in unreliables:
    node_unreliable[i] = True

edges = [] 
for i in range(num_edges):
    edge  = [int(x) for x in input().strip().split()]
    edges.append(edge)

#initialize with 0
adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

for edge in edges:
    vertex1 = edge[0]
    vertex2 = edge[1]
    weight = edge[2]

    adjacency_matrix[vertex1][vertex2] = weight
    adjacency_matrix[vertex2][vertex1] = weight

selected_node = [False for _ in range(num_vertices)]

no_edge = 0

# find the first reliable node to start with
for i in range(num_vertices):
    if not node_unreliable[i]:
        selected_node[i] = True
        break

vertices_selected = [False for _ in range(num_vertices)]

total_cost = 0
while (no_edge < num_vertices - 1):
    minimum = float('inf')
    a = num_vertices
    b = num_vertices
    for m in range(num_vertices):
        if node_unreliable[m]:
            continue

        if selected_node[m]:
            for n in range(num_vertices):
                if ((not selected_node[n]) and adjacency_matrix[m][n]):  
                    # not in selected and there is an edge
                    if not node_unreliable[n] and minimum > adjacency_matrix[m][n]:
                        minimum = adjacency_matrix[m][n]
                        a = m
                        b = n

    if a != num_vertices:
        total_cost += adjacency_matrix[a][b]
        selected_node[b] = True
    no_edge += 1

# go through all the unreliable spies and add the cheapest edge that doesn't connect to another unreliable spy
for i in range(len(adjacency_matrix)):
    if node_unreliable[i]:
        min = float('inf')
        for j in range(len(adjacency_matrix[i])):
            if not node_unreliable[j] and adjacency_matrix[i][j] > 0 and min > adjacency_matrix[i][j]:
                min = adjacency_matrix[i][j]
        total_cost += min

graph_complete = True
for i in range(num_vertices):
    if not node_unreliable[i] and not selected_node[i]:
        graph_complete = False

if graph_complete:
    print(total_cost)
else:
    print("NONE")