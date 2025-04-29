from collections import deque

def bfs(adj):
    V = len(adj)
    res = []
    visited = [False] * V
    q = deque([0])
    visited[0] = True

    while q:
        curr = q.popleft()
        res.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return res

if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    adj = [[] for _ in range(V)]
    print("Enter each edge (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)  # for undirected graph

    ans = bfs(adj)
    print("BFS Traversal:", *ans)
