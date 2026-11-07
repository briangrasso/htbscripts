import sys
import heapq

def solve_pivot_chain():
    # Read all non-empty lines from standard input
    input_data = [line.strip() for line in sys.stdin if line.strip()]
    if not input_data:
        return

    # 1. Parse the configuration line
    config_line = input_data[0].split()
    num_nodes = int(config_line[0])
    num_edges = int(config_line[1])
    start_node = config_line[2]
    target_node = config_line[3]

    # 2. Build the graph adjacency list
    graph = {}
    # Process only the number of edge lines specified
    for i in range(1, num_edges + 1):
        if i < len(input_data):
            u, v, w = input_data[i].split()
            weight = int(w)
            
            if u not in graph:
                graph[u] = []
            graph[u].append((v, weight))

    # 3. Dijkstra's Algorithm (Optimized for tracking lowest total cost)
    queue = [(0, start_node)]
    visited = {}

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        # If we reached the target, this is guaranteed to be the lowest cost path
        if current_node == target_node:
            print(current_cost)
            return

        if current_node in visited and visited[current_node] <= current_cost:
            continue
            
        visited[current_node] = current_cost

        for neighbor, weight in graph.get(current_node, []):
            next_cost = current_cost + weight
            if neighbor not in visited or next_cost < visited[neighbor]:
                heapq.heappush(queue, (next_cost, neighbor))

    # Fallback if no valid path exists
    print(-1)

if __name__ == "__main__":
    solve_pivot_chain()
