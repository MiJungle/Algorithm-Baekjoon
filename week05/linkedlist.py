from requests import head


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 =Node(1)
head = node1
for index in range(2,10):
    add(index)

node = head
while node.next:
    print(node.data)
    node = node.next#옆 노드로 옮겨가는 것임 
print(node.data)