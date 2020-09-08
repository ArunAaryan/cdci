from LinkedList import LinkedList, Node

def findLength(node):
    count = 0
    while node:
        count += 1
        node = node.next 
    return count, node

def findIntersection(list1, list2):
    l1, node1= findLength(list1)
    l2, node2 = findLength(list2)
    if node1 != node2:
        return None 
    if l1 > l2:
        longlist = list1 
        shortlist = list2 
    else:
        shortlist = list1
        longlist = list2 
        
    diffLen = abs(l1 - l2)
    while(diffLen>0):
        longlist = longlist.next 
        diffLen -= 1
    while shortlist and longlist:
        if shortlist == longlist:
            return shortlist
        shortlist = shortlist.next 
        longlist = longlist.next 
    return None

       
l = LinkedList()
head1 = l.addNode(1)
l.addNode(2)
head, node3 = l.addNode(3)
l.addNode(4)
l.addNode(8)



l2 = LinkedList()
head2= l2.addNode(9)
head, node2 = l2.addNode(8)
node2.next = node3

result = findIntersection(head1, head2)
print(result.data)