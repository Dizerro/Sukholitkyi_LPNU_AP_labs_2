def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])

def is_root_vertex(graph, start, n):
    visited = [False] * n
    dfs(graph, start, visited)
    return all(visited)

def find_all_roots(graph, n):
    roots = []
    for i in range(n):
        if is_root_vertex(graph, i, n):
            roots.append(i)
    return roots if roots else [-1]

def read_graph_from_file(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        graph = [[] for _ in range(n)]
        for line in f:
            u, v = map(int, line.strip().split())
            graph[u].append(v)
    return graph, n

def write_output(filename, roots):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, roots)))

graph, n = read_graph_from_file("input.txt")
roots = find_all_roots(graph, n)
write_output("output.txt", roots)