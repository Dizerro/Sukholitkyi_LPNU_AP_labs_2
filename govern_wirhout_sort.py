def main():
    with open("govern.in", "r") as file:
        lines = file.read().splitlines()

    graph = {}
    in_degree = {}
    nodes = set()

    for line in lines:
        a, b = line.split()
        nodes.add(a)
        nodes.add(b)

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[b].append(a)

        if a not in in_degree:
            in_degree[a] = 0
        if b not in in_degree:
            in_degree[b] = 0
        in_degree[a] += 1

    queue = []
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    result = []

    while queue:
        current = queue.pop()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    with open("govern.out", "w") as file:
        for name in result:
            file.write(name + "\n")

    with open("nodes.out", "w") as file:
        for name in sorted(nodes):
            file.write(name + "\n")

main()