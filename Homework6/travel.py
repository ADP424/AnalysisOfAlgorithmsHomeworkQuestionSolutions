num_travel_locations = int(input())
num_travel_edges = int(input())
money_budget = int(input())
time_budget = int(input())

# each index represented a list of edges adjacent to each location (vertex) from 0...num_travel_locations
# each element is a list of tuples in the form (adjacent location, monetary cost, time cost)
adjacencies = [[] for _ in range(num_travel_locations)]

# read in all the edges into the adjacency list
# takes O(m) time
for i in range(num_travel_edges):
    edge = [int(i) for i in input().split(' ')]
    adjacencies[edge[0]].append((edge[1], edge[2], edge[3]))
    adjacencies[edge[1]].append((edge[0], edge[2], edge[3]))

# Dijkstra's algorithm distance matrix for money costs
money_costs = [float('inf') for _ in range(num_travel_locations)]
money_costs[0] = 0

# Dijkstra's algorithm distance matrix for time costs
time_costs = [float('inf') for _ in range(num_travel_locations)]
time_costs[0] = 0

# Dijkstra's algorithm prev matrix for money costs
previous_location_money = [-1 for _ in range(num_travel_locations)]

# Dijkstra's algorithm prev matrix for time costs
previous_location_time = [-1 for _ in range(num_travel_locations)]

queue = []

# iterate through the locations to find the path with the minimum monetary cost
for i in range(num_travel_locations):
    queue.append(i)

while len(queue) != 0:
    # get the location with the lowest distance so far and remove it from the queue
    # takes O(n) time (this is a problem! :/)
    min_location = queue[0]
    for location in queue:
        if money_costs[min_location] > money_costs[location]:
            min_location = location
    queue.remove(min_location)

    for neighboring_edge in adjacencies[min_location]:
        alternative_route = money_costs[min_location] + neighboring_edge[1]
        alternative_route_time = time_costs[min_location] + neighboring_edge[2]
        if alternative_route < money_costs[neighboring_edge[0]] and alternative_route_time <= time_budget:
            money_costs[neighboring_edge[0]] = alternative_route
            time_costs[neighboring_edge[0]] = alternative_route_time
            #previous_location_money[neighboring_edge[0]] = min_location

print(money_costs[num_travel_locations - 1])
print(time_costs[num_travel_locations - 1])

if money_costs[num_travel_locations - 1] <= money_budget and time_costs[num_travel_locations - 1] <= time_budget:
    print("YES")
else:
    # reset the money costs array
    money_costs = [float('inf') for _ in range(num_travel_locations)]
    money_costs[0] = 0

    # reset the time costs array
    time_costs = [float('inf') for _ in range(num_travel_locations)]
    time_costs[0] = 0

    # iterate through the locations to find the path with the minimum time cost
    for i in range(num_travel_locations):
        queue.append(i)

    while len(queue) != 0:
        # get the location with the lowest distance so far and remove it from the queue
        # takes O(n) time (this is a problem! :/)
        min_location = queue[0]
        for location in queue:
            if time_costs[min_location] > time_costs[location]:
                min_location = location
        queue.remove(min_location)

        for neighboring_edge in adjacencies[min_location]:
            alternative_route = time_costs[min_location] + neighboring_edge[2]
            alternative_route_money = money_costs[min_location] + neighboring_edge[1]
            if alternative_route < time_costs[neighboring_edge[0]] and alternative_route_money <= money_budget:
                time_costs[neighboring_edge[0]] = alternative_route
                money_costs[neighboring_edge[0]] = alternative_route_money
                #previous_location_money[neighboring_edge[0]] = min_location

    print(money_costs[num_travel_locations - 1])
    print(time_costs[num_travel_locations - 1])
    
    if money_costs[num_travel_locations - 1] <= money_budget and time_costs[num_travel_locations - 1] <= time_budget:
        print("YES")
    else:
        print("NO")