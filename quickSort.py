# Import modules to be used
from random import randint
import numpy as np
import time
import csv

#From: https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python

def quicksort(array):
    # If the input array contains less than two elements,
    # then return it as an array with only one element can't be sorted
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Randomly select an element to 'Pivot' on (not including the first or last element)
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # Quicksort is recursively called on the 'low' and 'high' 
    # lists and then they are joined, with 'same' in the middle
    return quicksort(low) + same + quicksort(high)


# Initialise the random generator
rng = np.random.default_rng()

# empty array to contain sorting times
test= []
# Function to allow multiple input instances 
def runs(noRuns):
    # Loop through list of input sizes
    for x in noRuns:
        # fetches current number of seconds since epoch
        start_time = time.time()
        # call the sorting function
        quicksort(rng.integers(low=0, high=10, size=x))
        # fetches current number of seconds since epoch
        end_time = time.time()
        # subtract start and end times to get the elapsed time
        time_elapsed = end_time - start_time
        # add this time to the array
        test.append(time_elapsed)
    


# Run the test 10 times
for x in range(10): 
    runs([100, 200, 500,750, 1000, 1250,2500, 3750, 5000, 6250, 7500, 8750, 10000])

# reshape the array to 2 dimensions
test= np.reshape(test, (10, 13))


# print mean of columns
print(test.mean(axis=0))

# Open the times.csv file and append what comes next
with open('times.csv', 'a') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(test.mean(axis=0))