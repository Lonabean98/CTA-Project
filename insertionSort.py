from random import randint
import numpy as np
import timeit
import time
import csv

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

rng = np.random.default_rng()
 
test= []
def runs(noRuns):
    
    for x in noRuns:
        
        start_time = time.time()
        # call your function
        insertion_sort(rng.integers(low=0, high=10, size=x))
        end_time = time.time()
        time_elapsed = end_time - start_time
        test.append(time_elapsed)
    


# Run the test 10 times
for x in range(10): 
    runs([100, 200, 500,750, 1000])

# reshape the array to 2 dimensions
test= np.reshape(test, (10, 5))


# print mean of columns
print(test.mean(axis=0))


with open('times.csv', 'a') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(test.mean(axis=0))