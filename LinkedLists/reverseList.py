from LinkedList import LinkedList, Node 

new_list = LinkedList()
head = new_list.addNode(1)
new_list.addNode(2)
new_list.addNode(3)
new_list.addNode(4)
reverseList(head)
new_list.printList()