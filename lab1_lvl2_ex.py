def snake_order(matrix):
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    
    for col in range(n - 1, -1, -1):
        if (n - 1 - col) % 2 == 0:
            for row in range(m):
                result.append(matrix[row][col])
        else:

                result.append(matrix[row][col])
    
    return result

matrix = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

print(snake_order(matrix))