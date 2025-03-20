def snake_order(matrix):
    result = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(reversed(row))
    return result