def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfsRec(adj, visited, i, res)

def DFS(adj):
    visited = [0]*len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res

def add_edge(adj, s, t):
    adj[s][t] = adj[t][s] = 1

if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    adj = [[0]*V for _ in range(V)]
    print("Enter edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        add_edge(adj, u, v)
    res = DFS(adj)
    print("DFS Traversal:", *res)
