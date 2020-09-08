from LinkedList import LinkedList, Node

def detectCycle(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            break 
    if fast == None or fast.next == None:
        return None 
    
    slow = head 
    while slow != fast:
        slow = slow.next 
        fast = fast.next 
    return slow

l = LinkedList()
head = l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
l.addNode(6)
h, cp = l.addNode(7)
l.addNode(8)
l.addNode(9)
l.addNode(10)
h, p = l.addNode(11)
p.next = cp

collisionPoint = detectCycle(head)
print(collisionPoint.data)