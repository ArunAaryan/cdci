class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
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
        return (self.head, new_node) 


    def printList(self):
        cur = self.head
        while(cur):
            print(cur.data,end=' ')
            cur = cur.next 
        print('\n')
    def reverseList(self):
        next = None
        current = self.head 
        prev = None
        while(current):
            next = current.next 
            current.next = prev 
            prev = current
            current = next 
        self.head = prev
# list = LinkedList()
# list.node(1)
# list.addNode(2)
# list.addNode(3)
# list.addNode(4)
# list.reverseList()
# list.printList()
