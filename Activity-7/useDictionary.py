# This program uses a Python dictionary to find the mode(s) of a data set.

# The mode of a data set is its most frequently occurring value.
# A data set may have more than one mode.
# Examples:
#  mode of [1,2,3,4,5,6,7] is none
#  mode of [1,2,3,4,5,6,7,7] is 7
#  modes of [1,2,2,2,3,3,4,5,6,7,7,7] are 2 and 7

# Replace any "<your code>" comments with your own code statement(s)
# to accomplish the specified task.
# Do not change any other code.

# This function returns a list containing the mode or modes of the data set.
# Input:
#   data - a list of data values.
# Output:
#   returns a list with the value or values that are the mode of data.
#   If there is no mode, the returned list is empty.
def mode(data):
    dictionary = {}

    # Part 1:
    # Update dictionary so that each dictionary key is a value in data and
    # each dictionary value is the correspinding number of times that value occurs:
    # <your code>

    for value in data:
        if value in dictionary.keys():
            dictionary[value] += 1
        else:
            dictionary[value] = 1

    # Part 2:
    # Find the maximum of the dictionary values:
    # <your code>

    maximum = max(dictionary.values())

    # Part 3:
    # Create a list of the keys that have the maximum value:
    modes = []
    # <your code>

    for key, values in dictionary.items():
        if values == maximum:
            modes.append(key)

    # Part 4:
    # If no item occurs more than the others, then there is no mode:
    # <your code>

    if len(modes) == len(data):
        return[]
    else:
        return modes

data1 = [1,2,3,4,5,6,7]
print(data1)
print("mode:", mode(data1))
print()

data2 = [1,2,3,4,5,6,7,7]
print(data2)
print("mode:", mode(data2))
print()

data3 = [1,2,2,2,3,3,4,5,6,7,7,7]
print(data3)
print("mode:", mode(data3))
print()

data4 = ["blue", "red", "green", "blue", "orange", "yellow", "green"]
print(data4)
print("mode:", mode(data4))
print()

