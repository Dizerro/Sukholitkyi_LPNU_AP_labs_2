def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def parse_input(lines):
    graph = {}
    all_docs_set = set()

    for line in lines:
        a, b = line.strip().split()

        if b not in graph:
            graph[b] = []
        graph[b].append(a)

        all_docs_set.add(a)
        all_docs_set.add(b)

    all_docs = list(all_docs_set)

    for doc in graph:
        graph[doc] = merge_sort(graph[doc])

    all_docs = merge_sort(all_docs)
    return graph, all_docs


def topological_sort(graph, all_docs):
    visited = {}
    result = []

    def dfs(doc):
        visited[doc] = True
        if doc in graph:
            for neighbor in graph[doc]:
                if neighbor not in visited:
                    dfs(neighbor)
        result.append(doc)

    for doc in all_docs:
        if doc not in visited:
            dfs(doc)

    result.reverse()
    return result


def process_dependencies(lines):
    graph, all_docs = parse_input(lines)
    return topological_sort(graph, all_docs)


if __name__ == "__main__":
    with open("govern.in", "r") as f:
        lines = f.readlines()

    result = process_dependencies(lines)

    with open("govern.out", "w") as f:
        for doc in result:
            f.write(doc + "\n")
