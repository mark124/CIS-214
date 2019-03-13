# This program exercises arrays and linked lists of nodes.

# Replace any "<your code>" comments with your own code statement(s)
# to accomplish the specified task.
# Do not change any other code.

# The following files must be in the same folder:
#   arrays.py
#   node.py

from arrays import Array
from node import Node

# Here is the array:
theArray = Array(10)
for i in range(len(theArray)):
    theArray[i] = i + 1

# Print the array:
print("The array structure:")
print(theArray)

head = Node(theArray[0], None)
tail = head

# Part 1:
# Copy the array items to a linked structure:
# The linked structure must consist of Node class items.
# You must use some form of a loop to create the linked structure.
#<your code>


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

head = None
for i in range(len(theArray))[::-1]:
    head = Node(theArray[i], head)
    
    
print() # blank line

# Part 2:
print("The linked structure:")
# Print the linked structure with each item on a separate line.
# You must use some form of a loop to print the linked structure.
#<your code>


while head != None:
    print(head.data)
    head = head.next
