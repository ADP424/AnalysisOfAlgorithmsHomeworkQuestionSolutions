from heapq import heappush, heappop

def travel_within_budget(n, monetary_budget, time_budget, edges):
    graph = [[] for _ in range(n)]
    for edge in edges:
        first_vertex = edge[0]
        second_vertex = edge[1]
        cost = edge[2]
        time = edge[3]
        graph[first_vertex].append((second_vertex, cost, time))
        graph[second_vertex].append((first_vertex, cost, time))
    
    visited = set()
    priority_queue = [(0, 0, 0)]  # (total_cost, current_node, time_spent)

    while priority_queue:
        temp_node = heappop(priority_queue)
        total_cost = temp_node[0]
        current_node = temp_node[1]
        time_spent = temp_node[2]
        
        if (current_node, time_spent) in visited: 
            continue

        visited.add((current_node, time_spent))

        if current_node == n - 1 and total_cost <= monetary_budget \
            and time_spent <= time_budget:
            return "YES"

        for neighbor, cost, time in graph[current_node]:
            next_cost = total_cost + cost
            next_time = time_spent + time

            if (next_cost <= monetary_budget and next_time <= time_budget \
                and (neighbor, next_time) not in visited):
                heappush(priority_queue, (next_cost, neighbor, next_time))
    
    return "NO"

def main():
    n = int(input())
    m = int(input())
    monetary_budget = int(input())
    time_budget = int(input())

    edges = []
    for _ in range(m):
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    
    result = travel_within_budget(n, monetary_budget, time_budget, edges)
    print(result)

main()