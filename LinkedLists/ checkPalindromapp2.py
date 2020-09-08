from LinkedList import LinkedList, Node 
from collections import deque
def checkPalindrome(head):
    prevElements = deque()
    fast = head 
    slow = head 
    while( fast and fast.next ):
        prevElements.append(slow.data)
        slow = slow.next 
        fast = fast.next.next 
    
    if fast:
        slow = slow.next 

    while slow:
        if slow.data != prevElements.pop():
            return False
        slow = slow.next 
    return True

l = LinkedList()    
head = l.addNode(3)
l.addNode(4)
l.addNode(3)
# l.printList()
print(checkPalindrome(head))