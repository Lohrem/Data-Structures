"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    def __len__(self):
        return self.size

    def enqueue(self, val):
        self.storage.add_to_tail(val)
        self.size += 1
    def dequeue(self):
        if not self.size:
            return None
        self.size -= 1
        the_value_that_was_taken_out = self.storage.remove_from_head()
        return the_value_that_was_taken_out

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def isEmpty(self):
#         return self.storage == []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         self.size += 1

#     def dequeue(self):
#         if not self.size:
#             return None
#         self.size -= 1
#         return self.storage.pop()
