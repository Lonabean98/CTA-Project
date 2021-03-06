from tkinter import Y
import numpy as np
import time
import numpy as np
import csv




# From: https://stackabuse.com/bubble-sort-in-python/

def bubble_sort(our_list):
    # Go through the array as many times as there are elements in the array
    for i in range(len(our_list)):
        # Go through the array up to the second last element
        for j in range(len(our_list) - 1):
            # If the element before the next element is larger...
            if our_list[j] > our_list[j+1]:
                # Swap their positions
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

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
        bubble_sort(rng.integers(low=0, high=10, size=x))
        # fetches current number of seconds since epoch
        end_time = time.time()
        # subtract start and end times to get the elapsed time
        time_elapsed = end_time - start_time
        # add this time to the array
        test.append(time_elapsed)
    


# Run the test 10 times
for x in range(2): 
    runs([100, 200, 500,750, 1000, 1250,2500, 3750, 5000, 6250, 7500, 8750, 10000])

# reshape the array to 2 dimensions
test= np.reshape(test, (2, 13))


# print mean of columns
print(test.mean(axis=0))

# Open the times.csv file and append what comes next
with open('times.csv', 'a') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(test.mean(axis=0))

