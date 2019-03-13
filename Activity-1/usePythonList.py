# This program exercises Python built-in lists.

# Replace any "<your code>" comments with your own code statement(s)
# to accomplish the specified task.
# Do not change any other code.

# Here is your starting list: 
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the list:
print("myList:")
print(myList)

# Part 1:
# Print the items at indexes 0, 5, and 9:
print()
print("Items at indexes 0, 5, and 9:")
print(myList[0]) ###
print(myList[5]) ###
print(myList[9]) ###

# Part 2:
# Use the len() function to print the number of items in the list:
print()
print("Length of list:")
print(len(myList)) ###

# Part 3:
# Use the append() method to add the number 5 to the end of the list:
print()
print("Using append() to add the number 5 to the end of the list:")
myList.append(5) ###
print(myList)

# Print the number of items in the list:
print()
print("Length of list:")
print(len(myList))

# Part 4:
# Use the count() method to print the number of times
# the number 5 occurs in the list:
print()
print("Using count() to find the number of times 5 occurs in the list:")
print(myList.count(5)) ###
# Make sure your code prints your result.

# Part 5:
# Use the pop() method to remove the last item from the list:
# The last item is the one at index len(myList) - 1.
print()
print("Using pop() to remove the last item from the list:")
myList.pop(len(myList) - 1) ###
print(myList)

# Part 6:
# Use the remove() method to remove the number 7 from the list:
# This will remove the first (and only) 7 it finds.
print()
print("Using remove() to remove the number 7 from the list:")
myList.remove(7) ###
print(myList)

# Part 7:
# Use the insert() method to insert the number 7 back in the list:
# Insert it where it is supposed to go, which is at index 6.
print()
print("Using insert() to insert the number 7 back in the list:")
myList.insert(6, 7) ###(index, value)
print(myList)

# Part 8:
# Use the index() method to find the index of the number 7 in the list:
# This will be for the first (and only) 7 it finds.
print()
print("Using index() to find the index of the number 7 in the list:")
print(myList.index(7)) ###
# Make sure your code prints your result.

# Part 9:
# Use the min() function to find the smallest item in the list:
print()
print("Using min() to find the smallest item in the list:")
print(min(myList)) ###
# Make sure your code prints your result.

# Part 10:
# Use the max() function to find the largest item in the list:
print()
print("Using max() to find the largest item in the list:")
print(max(myList)) ###
# Make sure your code prints your result.

# Part 11:
# Use the "in" operation to determine whether the number 7 is in the list:
print()
print("Using \"in\" to determine whether the number 7 is in the list:")    
print('True' if 7 in myList else 'False') ###
# Make sure your code prints your result.

# Part 12:
# Use the "in" operation to determine whether the number 11 is in the list:
print()
print("Using \"in\" to determine whether the number 11 is in the list:")
print('True' if 11 in myList else 'False') ###
# Make sure your code prints your result.

# Part 13:
# Use the following kind of "for" loop
#   for x in myList:
# to print each item in the list on a separate line:
print()
print("Each item in list on a separate line:")
for x in myList: ###
    print(x)     ###
# Make sure your code prints your result.

# Part 14:
# Use a "for" loop to add 10 to each item in the list:
# Your "for" statement should be:
#   for i in range(len(myList)):
# Inside your "for" loop you will use "i" as an index
# to reference the corresponding list item.
#
# NOTE: The following code will NOT work here.
##for x in myList:
##    x += 10
# The reason is because numbers are immutable and each
# list entry itself is not changed.
# Only the x references are changed.
#
print()
print("Add 10 to each item in the list:")
for i in range(len(myList)): ###
    myList[i] += 10          ###
print(myList)

# Part 15:
# Use a "for" loop to subtract 10 from each item in the list:
print()
print("Subtract 10 from each item in the list:")
for i in range(len(myList)): ###
    myList[i] -= 10
print(myList)

# Part 16:
# Use the reverse() method to reverse the items in the list:
print()
print("Using reverse() to reverse the items in the list:")
myList.reverse() ###
print(myList)

# Part 17:
# Use the sort() method to sort the items in the list:
# The items are to be sorted back into their original ascending order.
print()
print("Using sort() to sort the items in the list:")
myList.sort() ###
print(myList)

# Use the copy() method to create a shallow copy of the list:
# Name your copy copyList.
# Shallow copies can lead to problems when the items are mutable.
# For our list, its number items are immutable (not mutable).
print()
print("Using copy() to create a shallow copy of the list:")
copyList = myList.copy()
print(copyList)

# Part 18:
# Use the clear() method to remove all the items from myList:
print()
print("Using clear() to remove all the items from myList:")
myList.clear() ###
print("myList:", myList)
print("copyList:",copyList)

# Part 19:
# Use the extend() method to extend myList with the contents of copyList:
print()
print("Using extend() to extend myList with the contents of copyList:")
myList.extend(copyList) ###
print("myList:", myList)
print("copyList:",copyList)

