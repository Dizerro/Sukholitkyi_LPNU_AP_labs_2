class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        node = Node(value, priority)
        self.root = self._insert(self.root, node)

    def _insert(self, current, node):
        if current is None:
            return node
        if node.priority > current.priority:
            node, current = current, node
        if current.left is None:
            current.left = self._insert(current.left, node)
        elif current.right is None:
            current.right = self._insert(current.right, node)
        else:
            if self._get_size(current.left) <= self._get_size(current.right):
                current.left = self._insert(current.left, node)
            else:
                current.right = self._insert(current.right, node)
        return current

    def _get_size(self, node):
        if node is None:
            return 0
        return 1 + self._get_size(node.left) + self._get_size(node.right)

    def peek(self):
        if self.root is None:
            return None
        return (self.root.value, self.root.priority)

    def extract_max(self):
        if self.root is None:
            return None
        max_node = self.root
        self.root = self._merge(self.root.left, self.root.right)
        return (max_node.value, max_node.priority)

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.priority >= right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    def print_tree(self):
        levels = []
        self._traverse(self.root, 0, levels)
        for level in levels:
            print(" | ".join(f"{n.value}:{n.priority}" for n in level))

    def _traverse(self, node, depth, levels):
        if node is None:
            return
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(node)
        self._traverse(node.left, depth + 1, levels)
        self._traverse(node.right, depth + 1, levels)

if __name__ == "__main__":
    queue = PriorityQueue()

    queue.insert("A", 3)
    queue.insert("B", 5)
    queue.insert("C", 1)
    queue.insert("D", 4)
    queue.insert("E", 2)

    print("Черга після вставок:")
    queue.print_tree()

    print("\n Найвищий пріоритет (peek):")
    print(queue.peek())

    print("\n Видаляємо елемент з найвищим пріоритетом:")
    print(queue.extract_max())

    print("\n Черга після видалення:")
    queue.print_tree()

    print("\n Ще одне видалення:")
    print(queue.extract_max())

    print("\n Черга після другого видалення:")
    queue.print_tree()
