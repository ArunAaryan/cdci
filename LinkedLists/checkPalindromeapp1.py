from LinkedList import LinkedList, Node 

def createReverseClone(head):
    new_head = None 
    while head:
        new_node = Node(head.data)
        new_node.next = new_head
        new_head = new_node 
        head = head.next 
    return new_head
def compareLists(list1, list2):
    while list1 and list2:
        if (list1.data != list2.data):
            return False
        list1 = list1.next 
        list2 = list2.next 
    return (list1==None and list2==None)  
l = LinkedList()    
head = l.addNode(3)
l.addNode(4)
l.addNode(4)
l.printList()
new_head = createReverseClone(head)
print(compareLists(new_head, head))
