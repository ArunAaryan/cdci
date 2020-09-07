from LinkedList import LinkedList, Node
def removeDuplicates(head):
    current = head
    present = set()
    prev = None
    while(current):
        if(current.data in present):
            prev.next = current.next 
        else:
            prev = current
            present.add(current.data)
        current = current.next 



list = LinkedList()
head = list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(3)
list.addNode(4)
list.printList()
removeDuplicates(head)
print('\n')
list.printList()
