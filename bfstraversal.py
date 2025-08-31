# BFS traversal implementation

from collections import deque

def bfs_traversal(start_node, graph):  
    # keeping track of visited nodes
    seen = [False for _ in range(len(graph))]   
    queue = deque()
    queue.append(start_node)   # enqueue the start
    seen[start_node] = True

    while len(queue) > 0:   
        current = queue.popleft()
        print(current, end=" ")   

        # neighbors of the current node
        for nxt in graph[current]:
            if not seen[nxt]:
                seen[nxt] = True
                queue.append(nxt)
            


if __name__ == "__main__":
    # example graph (undirected,)
    g = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2],
    }
    
    bfs_traversal(0, g)


