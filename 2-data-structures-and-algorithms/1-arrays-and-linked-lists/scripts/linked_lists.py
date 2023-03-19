class Node:
    def __init__(self):
        self.data = None
        self.next = None


head: Node | None = None
previous: Node | None = None
for i in range(5):
    node = Node()
    node.data = i

    if head is None:
        head = node

    if previous is not None:
        previous.next = node

    previous = node

current = head
while current is not None:
    print(current.data)
    current = current.next
