from LinkedList import LinkedList, Node
def kthToLast(head, k):
    if head == None:
        return 0
    index = kthToLast(head.next, k) + 1
    if index == k:
        print(head.data)
    return index 

list = LinkedList()
head = list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.printList()
kthToLast(head, 10)