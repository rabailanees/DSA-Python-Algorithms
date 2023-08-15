class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev=None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length += 1
    def pop(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
            self.length-=1
    def prepend(self, value):
        new_node = Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length += 1
    def pop_first(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
        else:
            temp=self.tail
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
            self.length-=1
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


            

my_doubly_linked_list = DoublyLinkedList()

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)
my_doubly_linked_list.prepend(1)
my_doubly_linked_list.pop_first()
print('Doubly Linked List:')
my_doubly_linked_list.print_list()
print('Get node from first half of DLL:')
print(my_doubly_linked_list.get(1).value)
my_doubly_linked_list.set_value(1,4)
my_doubly_linked_list.print_list()
my_doubly_linked_list.insert(4,4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()
print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

        