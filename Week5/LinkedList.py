class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_nodes(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count


# Example
print(count_nodes(None))
head = Node(42)
head.next = Node(67)
head.next.next = Node(24)

print(count_nodes(head))