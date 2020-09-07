#parition approach 1 by creating two lists and merging them later on.
from LinkedList import LinkedList, Node
def partition(head, x):
    first_start = None 
    second_start = None 
    first_end = None 
    second_end = None
    cur = head 
    while cur:
        next_node = cur.next
        cur.next =None
        if cur.data< x:
            if not first_start:
                first_start = cur
                first_end = first_start
            else:
                first_end.next = cur 
                first_end = cur 
        else:
            if not second_start:
                second_start = cur 
                second_end = cur
            else:
                second_end.next = cur
                second_end = cur
        cur = next_node

    if not first_start:
        return second_start
    
    first_end.next = second_start
    return first_start


l = LinkedList()
head = l.addNode(3)
l.addNode(5)
l.addNode(8)
l.addNode(5)
l.addNode(10)
l.addNode(2)
l.addNode(1)
new_list = partition(head, 8)
while(new_list):
    print(new_list.data, end = " ")
    new_list = new_list.next


