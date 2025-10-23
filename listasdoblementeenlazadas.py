from Node import Node
class listasdoblementeenlazadas
def __init__(self):
    self.head = None
    self.tail = None

def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

def str(self):
    nodes = []
    current = self.head
    while current:
        nodes.append(str(current.data))
        current = current.next
    return " <-> ".join(nodes)
    