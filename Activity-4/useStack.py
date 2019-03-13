# This program exercises stacks.

# Replace any "<your code>" comments with your own code statement(s)
# to accomplish the specified task.
# Do not change any other code.

# The following files must be in the same folder:
#   abstractcollection.py
#   abstractstack.py
#   arraystack.py
#   arrays.py
#   linkedstack.py
#   node.py

from arraystack import ArrayStack
from linkedstack import LinkedStack

def printStack1():
    print("stack1:", stack1)
    print()

def printStack2():
    print("stack2:", stack2)
    print()

def print2Stacks():
    print("stack1:", stack1)
    print("stack2:", stack2)
    print()

def print3Stacks():
    print("stack1:", stack1)
    print("stack2:", stack2)
    print("stack3:", stack3)
    print()

# Here are 2 starting stacks: 
stack1 = ArrayStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
stack2 = ArrayStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the stacks:
print2Stacks()

# Part 1:
# Use the == comparison operator to determine if the 2 stacks are equal.
# If they are equal print "The stacks are equal.".
# If they are not equal print "The stacks are not equal."
# <your code>

if stack1 == stack2:
    print("The stacks are equal.")
else:
    print("The stacks are not equal.")
    
print()

# Part 2:
# Remove the top item from stack1, print the removed item, and print stack1:
# <your code>

print(stack1.pop())

print("After removing the top item from stack1:")
printStack1()

# Part 3:
# Use the == comparison operator to determine if the 2 stacks are equal.
# If they are equal print "The stacks are equal.".
# If they are not equal print "The stacks are not equal."
# <your code>

if stack1 == stack2:
    print("The stacks are equal.")
else:
    print("The stacks are not equal.")
    
print()

# Part 4:
# Remove all the items from stack1 until there is only 3 items left in it:
# <your code>

n = 10
while n > 4:
    stack1.pop()
    n -= 1

print("After removing all but 3 items from stack1:")
printStack1()

# Part 5:
# Use a single method to empty stack1:
# <your code>

stack1.clear()

print("After emptying stack1:")
printStack1()

# Part 6:
# Use pop() and push() to move all even valued items from stack2 to stack1.
# This will leave stack2 empty.
# This will leave stack1 with only even valued items.
# stack1 will be in the reverse order from the original stack2 order.
# When popping, use a try/except block to catch and ignore the KeyError exception.
# <your code>

for i in range(0, len(stack2)):
    try:
        x = stack2.pop()
        if x % 2 == 0:
            stack1.push(x)
    except KeyError:
        pass
        
print("After moving evens to stack1 (in reverse order):")
print2Stacks()

# Part 7:
# Use pop() and push() to move all the stack1 items back to stack2.
# This will leave stack1 empty.
# This will leave stack2 with the even valued items back in their original order.
# You have effectively removed all the odd valued items from stack2.
# You will again need a try/except block.
# <your code>

for i in range(0, len(stack1)):
    try:
        x = stack1.pop()
        stack2.push(x)
    except KeyError:
        pass

print("After moving evens back to stack2 (in original order):")
print2Stacks()

# Part 8:
# Get and print the value at the top of stack2 without removing it:
# <your code>

item = stack2.peek()

print("The value at the top of stack2:", item)
printStack2()

# Part 9:
# Use isEmpty() to check whether stack1 and stack2 are empty.
# If either is empty, print a message saying it is empty.
# If either is not empty, print a message saying it is not empty.
# <your code>

if stack1.isEmpty() or stack2.isEmpty():
    print("stack1 is empty")
else:
    print("stack2 is not empty")

print()

# Part 10:
# Add the odd single-digit numbers to stack1 with 9 at the top:
# <your code>

for i in range(9, 0, -2):
    stack1.push(i)

print("After adding the odd single-digit numbers to stack1:")
print2Stacks()

# Part 11:
# Create a new empty stack of type LinkedStack called stack3:
stack3 = LinkedStack()
# Alternate popping items from stack2 and stack1, interleaving them onto stack3.
# Both stacks 1 and 2 will be left empty.
# As usual, handle or avoid exceptions.
# <your code>

i = 0
j = 0
while(i < len(stack1) and j < len(stack2)):
    stack3.push(stack2.pop())
    stack3.push(stack1.pop())

print("After moving items from stack1 and stack2 (interleaved) to stack3:")
print3Stacks()

# Part 12:
# Move each item from stack3 to both stack1 and stack2.
# Stacks 1 and 2 will be left in their original starting order.
# stack3 will be left empty.
# <your code>

for i in range(0, len(stack3)):
    element = stack3.pop()
    stack1.push(element)
    stack2.push(element)

print("After moving each item from stack3 to stacks 1 and 2:")
print3Stacks()



