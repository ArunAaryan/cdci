from LinkedList import LinkedList, Node
def partition(node, x):
    head = node 
    tail = node 
    while node:
        next_node = node.next
        if node.data < x:
            node.next = head 
            head = node 
        else:
            tail.next = node 
            tail = node 
        node = next_node
    tail.next = None 
    return head 

l = LinkedList()
head = l.addNode(3)
l.addNode(5)
l.addNode(8)
l.addNode(5)
l.addNode(10)
l.addNode(2)
l.addNode(5)
l.addNode(1)
l.printList()
new_head = partition(head, 5)
while(new_head):
    print(new_head.data, end = " ")    
    new_head = new_head.next
