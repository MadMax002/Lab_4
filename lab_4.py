def ford_fulkerson(graph, source, sink):
    def bfs(graph, source, sink, parent):
        visited = [False] * len(graph)
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == sink:
                        return True
        return False

    max_flow = 0
    parent = [-1] * len(graph)
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

with open("data3.txt") as f:
    graph = [[int(num) for num in line.split()] for line in f]
    source = 0
    sink = len(graph) - 1
    max_flow = ford_fulkerson(graph, source, sink)
    print("Max Flow:", max_flow)
