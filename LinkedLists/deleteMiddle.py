# delete node in the middle anything but first and last given access only to that node
from LinkedList import LinkedList, Node
def deleteMiddle(node):
    next_node = node.next 
    node.data = next_node.data  
    node.next = next_node.next

list = LinkedList()
list.addNode(1)
list.addNode(2)
head, del_node = list.addNode(3)
list.addNode(4)
list.printList()
deleteMiddle(del_node)
list.printList()
