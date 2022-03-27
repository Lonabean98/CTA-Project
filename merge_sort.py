import numpy as np
import timeit
import time
import csv





# From: https://www.educative.io/edpresso/merge-sort-in-python
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


rng = np.random.default_rng()
 
test= []
def runs(noRuns):
    
    for x in noRuns:
        
        start_time = time.time()
        # call your function
        mergeSort(rng.integers(low=0, high=10, size=x))
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
