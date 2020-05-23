"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = self.storage.length

    def __len__(self):
        return self.size

    def push(self, val):
        self.size = self.size + 1
        self.storage.add_to_tail(val)

    def pop(self):
        if not self.size:
            return None
        self.size -= 1

        the_value_that_was_taken_out_comma_yes_this_is_a_really_long_variable_name_because_im_bored_comma_anyways = self.storage.remove_from_tail()

        return the_value_that_was_taken_out_comma_yes_this_is_a_really_long_variable_name_because_im_bored_comma_anyways

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if not self.size:
#             return None
#         self.size -= 1
#         return self.storage.pop()
