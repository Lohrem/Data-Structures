class Node:
    def __init__(self, value=None, next=None):
        #get the value within the node
        pass

    def get_value(self):
        # get the next node in the list
        pass

    def get_next(self):
        #set next node in the list
        pass

    def set_next(self, new_next):
        #return a string of the value within the node
        pass

    def __str__(self):
        pass

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_tail(self, val):
        # what if the list is empty?
        pass

    def set_head(self, node):
        #doe the list contain a certain value, what is the logic needed for this?
        pass

    def contains(self, value):
        pass
    def remove_head(self):
        pass

    def get_max(self):
        pass
