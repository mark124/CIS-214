# This program exercises bags:

# Replace any "<your code>" comments with your own code statement(s)
# to accomplish the specified task.
# Do not change any other code.

# The following files must be in the same folder:
#   abstractcollection.py
#   abstractbag.py
#   arraybag.py
#   arrays.py
#   ball.py

from arraybag import ArrayBag
from ball import Ball

# Part 1:
# This function takes a bag that has red and blue balls in it
# and moves the balls to two other bags: one to hold the red
# balls and one to hold the blue balls.
#
# Preconditions:
#   bag - an ArrayBag containing zero or more red and blue Ball objects. 
#
# Postconditions:
#   returns - a bag containing the red balls and
#             a bag containing the blue balls.
#   The original bag should be emptied.
def distributeBag(bag):
    redBag = ArrayBag()
    blueBag = ArrayBag()

    # Move the balls to the appropriate bags:
    
    # <your code>


    
    for item in bag:

        if (item.getColor() == 'red'):
            redBag.add(item)
        elif (item.getColor() == 'blue'):
            blueBag.add(item)  
    bag.clear()
    

 
    # Return the 2 bags:
    return (redBag, blueBag)

# Part 2:
# This function prints the items in a bag, each on a separate line.
def printBag(bag):

    # <your code>

    
    for item in bag:
        str(item)
        print(item)
        
    if bag.isEmpty():
        print('empty')
    print()
        

    
# Test 1:
print("Test 1:")
bag1 = ArrayBag([Ball("red", 1),
                Ball("red", 2),
                Ball("red", 3),
                Ball("blue", 1),
                Ball("blue", 2),
                Ball("blue", 3)])
print("Original mixed bag:")
printBag(bag1)
redBag, blueBag = distributeBag(bag1)
print("Red bag:")
printBag(redBag)
print("Blue bag:")
printBag(blueBag)
print("Final mixed bag:")
printBag(bag1)

# Test 2:
print("Test 2:")
bag1 = ArrayBag([Ball("red", 1),
                Ball("red", 2),])
print("Original mixed bag:")
printBag(bag1)
redBag, blueBag = distributeBag(bag1)
print("Red bag:")
printBag(redBag)
print("Blue bag:")
printBag(blueBag)
print("Final mixed bag:")
printBag(bag1)

# Test 3:
print("Test 3:")
bag1 = ArrayBag()
print("Original mixed bag:")
printBag(bag1)
redBag, blueBag = distributeBag(bag1)
print("Red bag:")
printBag(redBag)
print("Blue bag:")
printBag(blueBag)
print("Final mixed bag:")
printBag(bag1)
