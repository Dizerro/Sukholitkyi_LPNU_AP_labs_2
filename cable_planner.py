def read_adjacency_matrix(file_path):
    matrix = []
    with open(file_path, "r") as file:
        for line in file:
            row = [int(x) for x in line.strip().split(",")]
            matrix.append(row)
    return matrix


def minimum_cable_length(matrix):
    n = len(matrix)
    selected = [False] * n
    edge_count = 0
    selected[0] = True
    total_weight = 0

    while edge_count < n - 1:
        minimum = float("inf")
        x =y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and matrix[i][j]:
                        if matrix[i][j] < minimum:
                            minimum = matrix[i][j]
                            x, y = i, j
        total_weight += minimum
        selected[y] = True
        edge_count += 1

    return total_weight

if __name__ == "__main__":
    file_path = "islands.csv"
    matrix = read_adjacency_matrix(file_path)
    result = minimum_cable_length(matrix)
    print("Мінімальна довжина кабелів:", result)