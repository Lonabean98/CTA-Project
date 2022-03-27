from tkinter import Y
import numpy as np
import timeit
import time
import statistics
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

rng = np.random.default_rng()
 
test= []
def runs(noRuns):
    
    for x in noRuns:
        
        start_time = time.time()
        # call your function
        bubble_sort(rng.integers(low=0, high=10, size=x))
        end_time = time.time()
        time_elapsed = end_time - start_time
        test.append(time_elapsed)
    


# Run the test 10 times
for x in range(10): 
    runs([100, 200, 500,750, 1000, 1250,2500, 3750, 5000, 6250, 7500, 8750, 10000])

# reshape the array to 2 dimensions
test= np.reshape(test, (10, 13))
#print(test)

# print mean of columns
print(test.mean(axis=0))

with open('times.csv', 'a') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(test.mean(axis=0))

