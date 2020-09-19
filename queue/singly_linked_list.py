# linear data structure made up of nodes and refs to the next node

# lets make some node class
class Node:
    def __init__(self, value, next_node = None):
        # value that the node is holding
        self.value = value
        # ref to the next node in the chain
        self.next_node = next_node
    

    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next

    


# now lets think of how we can make nodes interact in a way that consolidates their pieces together

# lets make a LinkedList class
# think of the idea of having a head and a tail like a snake 
# where the snake can grow based upon having more links in it

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def set_head(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node

    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.value)
            temp = temp.next_node

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)


# n1.set_next(n2) # n1.next_node = n2
# n1.get_value() # => 2