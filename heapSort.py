import numpy as np
import time
import csv

# From: https://www.programiz.com/dsa/heap-sort

def heapify(arr, n, i):
     # Find largest among root and children
     largest = i
     l = 2 * i + 1
     r = 2 * i + 2
 
     if l < n and arr[i] < arr[l]:
         largest = l
 
     if r < n and arr[largest] < arr[r]:
         largest = r
 
     # If root is not largest, swap with largest and recursively call heapify
     if largest != i:
         arr[i], arr[largest] = arr[largest], arr[i]
         heapify(arr, n, largest)
 
 
def heapSort(arr):
     n = len(arr)
 
     # Build max heap
     for i in range(n//2, -1, -1):
         heapify(arr, n, i)
 
     for i in range(n-1, 0, -1):
         # Swap
         arr[i], arr[0] = arr[0], arr[i]
 
         # Heapify root element
         heapify(arr, i, 0)


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
        heapSort(rng.integers(low=0, high=10, size=x))
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