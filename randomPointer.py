
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.random =None
    
class LinkedList:

    def __init__(self):
        self.head = None

    def addNode(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return self.head
        cur = self.head 
        while(cur.next):
            cur = cur.next 
        cur.next = new_node
        return (new_node) 


    def printList(self):
        cur = self.head
        while(cur):
            print(cur.data,end=' ')
            cur = cur.next 
        print('\n')

def addBetween(node):
    new_node = Node(node.data)
    new_node.next = node.next
    node.next = new_node
    return new_node

def randomPointerLinkedListClone(head):
    cur = head
    while(cur):
        new_dup = addBetween(cur) 
        if cur.random:
            new_dup.random = cur.random.next
        cur = cur.next.next 
    first = head
    second = first.next 
    second_head = first.next
    while first and first.next and second.next  :
        first.next = first.next.next
        second.next = second.next.next
        first = first.next
        second = second.next 
    first.next = None
    return second_head 

list = LinkedList()
head = list.addNode(1)
node2 = list.addNode(2)
node3 = list.addNode(3)
node4 = list.addNode(4)
head.random = node3
node3.random = node3
node4.random = node2
second_head = randomPointerLinkedListClone(head)
# list.printList()
# print(second_head.data)
# print(second_head.next.data)

# print(head.random.data)

while(head):
    print(head.data, end=' ')
    if(head.random):
        print(head.random.data)
    else:
        print('')
    head = head.next

while(second_head):
    print(second_head.data, end=' ')
    if(second_head.random):
        print(second_head.random.data)
    else:
        print('')
    second_head = second_head.next