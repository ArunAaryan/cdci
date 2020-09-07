from LinkedList import LinkedList, Node
def kthToLast(head, k):
    p1 = head 
    p2 = head 
    for i in range(k):
        if not head:
            return None 
        p1 = p1.next
    while p1:
        p1 = p1.next 
        p2 = p2.next 
    return p2 
list = LinkedList()
head = list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.printList()
node = kthToLast(head, 2)
print(node.data)