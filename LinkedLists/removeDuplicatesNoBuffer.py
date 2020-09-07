from LinkedList import LinkedList, Node

def removeDuplicates(head):
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.data == cur.data:
                runner.next = runner.next.next 
            else:
                runner = runner.next 
        cur = cur.next

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