import heapq 

# Dijkstra’s shortest path finder
def dijkstra_shortest(graph, source):
    n_nodes = len(graph)

    # starting with "infinity" distances, except for the source
    distances = [float("inf")] * n_nodes
    distances[source] = 0

    # priority queue (distance, node)
    todo = [(0, source)]

    while todo:
        cur_dist, cur_node = heapq.heappop(todo)

        if cur_dist > distances[cur_node]:
            continue
        for neighbor, weight in graph[cur_node]:
            new_dist = distances[cur_node] + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(todo, (new_dist, neighbor))

                # debug-ish: could print this, but leaving commented out
                # print(f"Updated dist of {neighbor} to {new_dist}")

    return distances   # return list of shortest paths from source


if __name__ == "__main__":
    # example graph (directed, weighted)
    g = {
        0: [(1, 2), (2, 4)],
        1: [(2, 1)],
        2: [(3, 7)],
        3: []  
    }

    print("Shortest paths from 0:", dijkstra_shortest(g, 0))
