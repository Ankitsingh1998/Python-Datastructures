#Data structure - Linked List
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)      

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)
s.add_at_end(6)
s.add_at_front(2)
s.add_at_end(4)
s.print_list()
print(s.get_last_node())

print(s.is_empty())


"""
Linked List --> a sequence of nodes
Node --> stores its own data and a link to next node.(one node is 
linked to other, forms like a linked chain.)
head --> first node, used as starting point for any iteration in 
the linked list.
--> The last node must have its link pointing to None to determine 
end of the list.
--> nodes can be inserted and removed from any position like simple 
list unlike stacks and queue.
--> Stacks, queues and graphs can also be created by using linked list.
--> add_at_front() method adds a new node as the head of the list and 
links it to previous head.
--> add_at_end() method iterates to end of the list using a while loop 
and adds the new node as the link of the last node.
"""
"""
Applications:
    --> when we have linked data like undo/redo functionality, the nodes 
    can represent the state with links to the previous and next states. 
    A playlist of music, where each clip is linked with next one.
"""