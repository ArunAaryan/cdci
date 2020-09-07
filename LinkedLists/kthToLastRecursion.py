# wrapper class Index to mimic call by reference like C++

from LinkedList import LinkedList, Node
class Index:
    val = 0
def ktolast(head, k):
    idx = Index()
    node = kthToLast(head, k, idx)
    return node

def kthToLast(head, k, val):
    if head == None:
        return None
    
    node = kthToLast(head.next, k, val)
    val.val += 1
    if val.val == k:
        return head 
    return node

list = LinkedList()
head = list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.printList()
node = ktolast(head, 2)
print(node.data)