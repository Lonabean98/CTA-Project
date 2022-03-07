import numpy as np
import timeit
import time


rng = np.random.default_rng()
list= rng.integers(low=0, high=10, size=50)


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

# Call the bubble algorithm with the unsorted array as the inputS
bubble_sort(list)
# Print the sorted array
print(list)


print()
start_time = time.time()
# call your function
bubble_sort(list)
end_time = time.time()
print(end_time - start_time)
print()



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


rng = np.random.default_rng(seed= 23)
list2= rng.integers(low=0, high=10, size=50)
mergeSort(list2)
print(list2)
