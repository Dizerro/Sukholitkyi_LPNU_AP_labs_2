def read_adjacency_matrix(filename):
    with open(filename) as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        row = [int(x.strip()) for x in line.strip().split(',')]
        matrix.append(row)
    return matrix

def create_canvas(width=40, height=25):
    return [[" " for _ in range(width)] for _ in range(height)]

def draw_nodes(canvas, positions, labels):
    for node, (x, y) in positions.items():
        if 0 <= y < len(canvas) and 0 <= x < len(canvas[0]):
            canvas[y][x] = labels[node]

def draw_edge(canvas, x1, y1, x2, y2, weight):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return
    for step in range(steps + 1):
        t = step / steps
        x = int(round(x1 + t * dx))
        y = int(round(y1 + t * dy))
        if 0 <= y < len(canvas) and 0 <= x < len(canvas[0]) and canvas[y][x] == " ":
            canvas[y][x] = "*"
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2
    w_str = str(weight)
    for i, ch in enumerate(w_str):
        if 0 <= mid_x + i < len(canvas[0]) and 0 <= mid_y < len(canvas):
            canvas[mid_y][mid_x + i] = ch

def generate_node_positions(n):
    positions = {}
    coords = [
        (20, 2),   # top
        (35, 8),   # top-right
        (30, 20),  # bottom-right
        (10, 20),  # bottom-left
        (5, 8),    # top-left
        (20, 12),  # center (for 6th)
    ]
    for i in range(n):
        if i < len(coords):
            positions[i] = coords[i]
        else:
            positions[i] = (2 * i + 2, 12)  # fallback: in ряд по центру
    return positions

def draw_ascii_graph(filename):
    matrix = read_adjacency_matrix(filename)
    n = len(matrix)
    labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    canvas = create_canvas()
    positions = generate_node_positions(n)
    draw_nodes(canvas, positions, labels)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                draw_edge(canvas, x1, y1, x2, y2, matrix[i][j])
    for row in canvas:
        print("".join(row))

draw_ascii_graph("islands.csv")